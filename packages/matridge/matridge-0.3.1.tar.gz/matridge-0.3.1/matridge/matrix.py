import logging
import time
import warnings
from asyncio import Task, create_task, sleep
from functools import wraps
from typing import TYPE_CHECKING, AsyncIterator, Awaitable, Callable, Optional, Union

import nio
from async_lru import alru_cache
from nio import Event
from slidge.core import config as global_config
from slidge.util.types import LegacyAttachment
from slixmpp import JID
from slixmpp.exceptions import XMPPError

from . import config
from .reactions import ReactionCache
from .util import Credentials, get_replace, server_timestamp_to_datetime

if TYPE_CHECKING:
    from .group import MUC, Participant
    from .session import Session


def catch_all(coro: Callable[["Client", nio.MatrixRoom, nio.Event], Awaitable[None]]):
    @wraps(coro)
    async def wrapped(self: "Client", room: nio.MatrixRoom, event: nio.Event, *a, **kw):
        event_id = getattr(event, "event_id", None)
        async with self.session.send_lock:
            if event_id in self.session.events_to_ignore:
                self.log.debug("Ignoring an event matridge has sent: %s", event_id)
                return
        try:
            return await coro(self, room, event, *a, **kw)
        except XMPPError as e:
            self.log.debug(
                "Exception raised in matrix client callback %s", coro, exc_info=e
            )
        except Exception as e:
            self.log.exception(
                "Exception raised in matrix client callback %s", coro, exc_info=e
            )

    return wrapped


class AuthenticationClient(nio.AsyncClient):
    def __init__(
        self, server: str, handle: str, jid: JID, log: Optional[logging.Logger] = None
    ):
        if not server.startswith("http"):
            server = "https://" + server
        self.store_path = store_path = global_config.HOME_DIR / (jid.bare + "_state")
        store_path.mkdir(exist_ok=True)
        cfg = nio.AsyncClientConfig(
            store_sync_tokens=True,
            max_limit_exceeded=0,
            max_timeouts=0,
            encryption_enabled=True,
        )
        super().__init__(server, handle, store_path=str(store_path), config=cfg)
        if log:
            self.log = log
        else:
            self.log = logging.getLogger(__name__)

    def get_credentials(self, resp: nio.LoginResponse) -> Credentials:
        return {
            "homeserver": self.homeserver,
            "user_id": resp.user_id,
            "device_id": resp.device_id,
            "access_token": resp.access_token,
        }

    async def fix_homeserver(self):
        """
        Uses https://$HOMESERVER/.well-known/matrix/client to fix the homeserver
        URL.
        """
        response = await self.discovery_info()
        if isinstance(response, nio.DiscoveryInfoResponse):
            self.homeserver = response.homeserver_url


class Client(AuthenticationClient):
    MIN_RETRY_TIME = 3
    MAX_RETRY_TIME = 300
    REQUEST_TIMEOUT = 30000
    CONSIDER_SUCCESSFUL = 10

    def __init__(self, server: str, handle: str, session: "Session"):
        super().__init__(server, handle, session.user.jid, session.log)
        self.__sync_task: Optional[Task] = None
        self.session = session
        self.reactions = ReactionCache(self)

    def load(self):
        stored = self.session.user.legacy_module_data
        self.access_token: str = stored["access_token"]  # type:ignore
        self.user_id: str = stored["user_id"]  # type:ignore
        self.device_id: str = stored["device_id"]  # type:ignore

    async def login_token(self):
        self.load()
        await self.fix_homeserver()
        self.load_store()

    def __add_event_handlers(self):
        self.add_event_callback(self.on_event, nio.Event)  # type:ignore
        self.add_event_callback(self.on_message, nio.RoomMessage)  # type:ignore
        self.add_event_callback(self.on_avatar, nio.RoomAvatarEvent)  # type:ignore
        self.add_event_callback(self.on_topic, nio.RoomTopicEvent)  # type:ignore
        self.add_event_callback(self.on_name, nio.RoomNameEvent)  # type:ignore
        self.add_event_callback(self.on_sticker, nio.StickerEvent)  # type:ignore
        self.add_event_callback(self.on_member, nio.RoomMemberEvent)  # type:ignore
        self.add_event_callback(self.on_redact, nio.RedactionEvent)  # type:ignore
        self.add_event_callback(self.on_reaction, nio.ReactionEvent)  # type:ignore
        self.add_event_callback(self.on_power_levels, nio.PowerLevelsEvent)  # type:ignore
        self.add_presence_callback(self.on_presence, nio.PresenceEvent)  # type:ignore
        self.add_ephemeral_callback(self.on_receipt, nio.ReceiptEvent)  # type:ignore
        self.add_ephemeral_callback(
            self.on_typing,  # type:ignore
            nio.TypingNoticeEvent,
        )

        self.add_to_device_callback(
            self.on_key_verification,  # type:ignore
            (nio.KeyVerificationEvent, nio.UnknownToDeviceEvent),
        )

    async def __get_muc(self, room: Union[nio.MatrixRoom, str]) -> "MUC":
        room_id = room.room_id if isinstance(room, nio.MatrixRoom) else room
        return await self.session.bookmarks.by_legacy_id(room_id)

    async def __sync_forever(self):
        attempts = 0
        while True:
            start = time.time()
            try:
                await self.sync_forever(timeout=self.REQUEST_TIMEOUT)
            except Exception as e:
                duration = time.time() - start
                if duration < self.CONSIDER_SUCCESSFUL:
                    attempts += 1
                    wait = min(attempts * self.MIN_RETRY_TIME, self.MAX_RETRY_TIME)
                else:
                    attempts = 0
                    wait = self.MIN_RETRY_TIME
                if attempts < 2:
                    self.log.debug(
                        "Sync task has raised %r, retrying in %s", e, wait, exc_info=e
                    )
                else:
                    self.log.error(
                        "Sync task has raised %r, retrying in %s", e, wait, exc_info=e
                    )
                await sleep(wait)
            else:
                break

    async def get_participant(
        self, room: nio.MatrixRoom, event: nio.Event
    ) -> "Participant":
        muc = await self.__get_muc(room)
        self.log.debug(
            "sender (%s) == me (%s)? %s",
            event.sender,
            self.session.contacts.user_legacy_id,
            event.sender == self.session.contacts.user_legacy_id,
        )
        return await muc.get_participant_by_legacy_id(event.sender)

    async def listen(self):
        # we need to sync full state or else we don't get the list of all rooms
        resp = await self.sync(full_state=True)
        self.log.debug("Sync")
        if isinstance(resp, nio.SyncError):
            raise PermissionError(resp)
        self.__add_event_handlers()
        self.__sync_task = create_task(self.__sync_forever())

    def stop_listen(self):
        if self.__sync_task is None:
            return
        self.__sync_task.cancel()

    async def fetch_history(self, room_id: str, limit: int) -> AsyncIterator[Event]:
        sync_resp = await self.sync()
        if isinstance(sync_resp, nio.SyncError):
            return
        resp = await self.room_messages(
            room_id,
            limit=limit,
            start=sync_resp.next_batch,
            message_filter={"types": ["m.room.message"]},
        )
        if not isinstance(resp, nio.RoomMessagesResponse):
            self.log.warning("Could not fill history.", sync_resp)
            return
        for event in resp.chunk:
            yield event

    @catch_all
    async def on_event(self, room: nio.MatrixRoom, event: nio.Event):
        if config.NIO_VERBOSE:
            self.log.debug("Event %s '%s': %r", type(event), room, event)

    @catch_all
    async def on_message(self, room: nio.MatrixRoom, event: nio.RoomMessage):
        self.log.debug("Message: %s", event)

        participant = await self.get_participant(room, event)
        await participant.send_matrix_message(event)

    async def on_presence(self, presence: nio.PresenceEvent):
        if presence.user_id == self.session.contacts.user_legacy_id:
            return
        try:
            contact = await self.session.contacts.by_legacy_id(presence.user_id)
        except XMPPError as e:
            self.log.debug("Ignoring presence: %s", presence, exc_info=e)
            return
        contact.update_presence(presence)

    @catch_all
    async def on_avatar(self, room: nio.MatrixRoom, event: nio.RoomAvatarEvent):
        muc = await self.__get_muc(room)
        muc.avatar = event.avatar_url

    @catch_all
    async def on_topic(self, room: nio.MatrixRoom, event: nio.RoomTopicEvent):
        muc = await self.__get_muc(room)
        participant = await self.get_participant(room, event)
        muc.subject = event.topic
        muc.subject_setter = participant.name
        muc.subject_date = server_timestamp_to_datetime(event)

    @catch_all
    async def on_name(self, room: nio.MatrixRoom, event: nio.RoomNameEvent):
        muc = await self.__get_muc(room)
        muc.name = event.name

    @catch_all
    async def on_sticker(self, room: nio.MatrixRoom, event: nio.StickerEvent):
        participant = await self.get_participant(room, event)

        resp = await self.download(event.url)
        if isinstance(resp, nio.DownloadResponse):
            await participant.send_files(
                [LegacyAttachment(data=resp.body, caption=event.body)]
            )
        else:
            self.log.error("Failed to download sticker: %r", resp)

    @catch_all
    async def on_member(self, room: nio.MatrixRoom, event: nio.RoomMemberEvent):
        muc = await self.__get_muc(room)
        participant = await self.get_participant(room, event)
        if event.membership == "join" and participant.contact:
            participant.set_affiliation_from_power_level(
                room.power_levels.get_user_level(participant.contact.legacy_id)
            )
        elif event.membership == "leave":
            if participant.is_user:
                await self.session.bookmarks.remove(muc)
            else:
                muc.remove_participant(participant)
        elif event.membership == "ban":
            # TODO: handle bans in slidge core
            pass
        elif event.membership == "invite":
            # TODO: what's that event exactly?
            pass

    @catch_all
    async def on_typing(self, room: nio.MatrixRoom, event: nio.TypingNoticeEvent):
        muc = await self.__get_muc(room)
        for user_id in event.users:
            participant = await muc.get_participant_by_legacy_id(user_id)
            participant.composing()

    @catch_all
    async def on_receipt(self, room: nio.MatrixRoom, event: nio.ReceiptEvent):
        muc = await self.__get_muc(room)
        for receipt in event.receipts:
            if receipt.receipt_type == "m.read":
                participant = await muc.get_participant_by_legacy_id(receipt.user_id)
                participant.displayed(receipt.event_id)

    @catch_all
    async def on_reaction(self, room: nio.MatrixRoom, event: nio.ReactionEvent, **kw):
        self.log.debug("Reaction2")

        source = event.source
        msg_id = await self.get_original_id(room.room_id, event.reacts_to)

        sender = source["sender"]
        emoji = event.key

        with self.reactions.session() as s:
            reactions = await self.reactions.get(
                s, room.room_id, msg_id, sender, with_event_ids=True
            )

        event_ids = list(reactions.values())
        emojis = list(reactions.keys())
        if event.event_id in event_ids:
            idx = event_ids.index(event.event_id)
            stored_emoji = emojis[idx]
            if stored_emoji != emoji:
                warnings.warn(
                    f"Received an emoji reaction update for the event ID '{event.event_id}': "
                    f"'{stored_emoji}' → '{emoji}'. This is illegal in Matrix, ignoring."
                )
        else:
            if emoji in emojis:
                warnings.warn(
                    f"We already had an event ID for the emoji reaction '{emoji}':"
                    f" '{event.event_id}' → {reactions[emoji]}."
                )
            with self.reactions.session() as s:
                await self.reactions.add(
                    s, room.room_id, msg_id, sender, emoji, event.event_id
                )
                s.commit()
            if emoji in reactions:
                warnings.warn(
                    f"The emoji '{emoji}' was already present with a different event ID"
                )
            else:
                emojis.append(emoji)

        participant = await self.get_participant(room, event)
        participant.react(msg_id, emojis, **kw)

    @catch_all
    async def on_redact(self, room: nio.MatrixRoom, event: nio.RedactionEvent):
        self.log.debug("Redaction: %s", event)
        redacter = await self.get_participant(room, event)
        with self.reactions.session() as s:
            if reaction_target := self.reactions.remove(s, room.room_id, event.redacts):
                msg_id = await self.get_original_id(room.room_id, reaction_target.event)
                reactions = await self.reactions.get(
                    s, reaction_target.room, msg_id, event.sender
                )
                redacter.react(msg_id, reactions)
                s.commit()
                return

        redacted_event = await self.get_event(room.room_id, event.redacts)

        if redacted_event and event.sender == redacted_event.sender:
            redacter.retract(event.redacts)
        else:
            redacter.moderate(event.redacts, event.reason)

    async def on_power_levels(self, room: nio.MatrixRoom, event: nio.PowerLevelsEvent):
        muc = await self.__get_muc(room)
        for user_id, power_level in event.power_levels.users.items():
            participant = await muc.get_participant_by_legacy_id(user_id)
            participant.set_affiliation_from_power_level(power_level)

    @alru_cache(maxsize=1000)
    async def get_original_id(self, room_id: str, event_id: str) -> str:
        event = await self.get_event(room_id, event_id)
        if event is None:
            return event_id
        # no need to check recursively because replacements must refer to
        # the original event
        return get_replace(event.source) or event_id

    @alru_cache(maxsize=100)
    async def get_event(self, room_id: str, event_id: str) -> Optional[nio.Event]:
        resp = await self.session.matrix.room_get_event(room_id, event_id)
        if isinstance(resp, nio.RoomGetEventError):
            return None
        return resp.event

    async def on_key_verification(
        self, event: nio.KeyVerificationEvent | nio.UnknownToDeviceEvent
    ):
        # TODO: once https://github.com/matrix-nio/matrix-nio/issues/430 is fixed, we should be able to simplify
        #       this by ditching UnknownToDeviceEvent
        # Thanks to DomNomNom from the nio Channel,
        # cf https://github.com/wreald/matrix-nio/commit/5cb8e99965bcb622101b1d
        content = event.source.get("content", {})
        if event.source.get("type") == "m.key.verification.request":
            self.session.send_gateway_message(
                "Got verification request. Waiting for other device to accept SAS method…"
            )
            methods = content.get("methods")
            if "m.sas.v1" not in methods:
                self.session.send_gateway_message(
                    "Received a device verification request, but other device does not support SAS authentication. "
                    f"Methods: {methods}."
                )
                return
            txid = content.get("transaction_id")
            ready_event = nio.ToDeviceMessage(
                type="m.key.verification.ready",
                recipient=event.sender,
                recipient_device=content.get("from_device"),
                content={
                    "from_device": self.device_id,
                    "methods": ["m.sas.v1"],
                    "transaction_id": txid,
                },
            )
            resp = await self.to_device(ready_event, txid)
            if isinstance(resp, nio.ToDeviceError):
                self.session.send_gateway_message(f"to_device failed with {resp}")
        elif isinstance(event, nio.KeyVerificationStart):  # first step
            if "emoji" not in event.short_authentication_string:
                self.session.send_gateway_message(
                    "Received a device verification request, but other device does not support emoji verification "
                    f"{event.short_authentication_string}."
                )
                return
            resp = await self.accept_key_verification(event.transaction_id)
            if isinstance(resp, nio.ToDeviceError):
                self.session.send_gateway_message(
                    f"accept_key_verification failed with {resp}"
                )

            sas = self.key_verifications.get(event.transaction_id)

            if sas is None:
                self.session.send_gateway_message(f"transaction_id could not be found")
                return

            todevice_msg = sas.share_key()
            resp = await self.to_device(todevice_msg)
            if isinstance(resp, nio.ToDeviceError):
                self.session.send_gateway_message(f"❌ to_device failed with {resp}")

        elif isinstance(event, nio.KeyVerificationCancel):  # anytime
            self.session.send_gateway_message(
                f"Verification has been cancelled by {event.sender} "
                f'for reason "{event.reason}".'
            )

        elif isinstance(event, nio.KeyVerificationKey):  # second step
            sas = self.key_verifications.get(event.transaction_id)

            if sas is None:
                self.session.send_gateway_message(f"transaction_id could not be found")
                return

            self.session.send_gateway_message(f"{sas.get_emoji()}")

            yn = await self.session.input("Do the emojis match? (Y/N) (C for Cancel) ")
            if yn.lower() == "y":
                resp = await self.confirm_short_auth_string(event.transaction_id)
                if isinstance(resp, nio.ToDeviceError):
                    self.session.send_gateway_message(
                        f"confirm_short_auth_string failed with {resp}"
                    )

                # Extra step in new flow: once we have completed the SAS
                # verification successfully, send a 'done' to-device event
                # to the other device to assert that the verification was
                # successful.
                done_message = nio.ToDeviceMessage(
                    type="m.key.verification.done",
                    recipient=event.sender,
                    recipient_device=sas.other_olm_device.device_id,
                    content={
                        "transaction_id": sas.transaction_id,
                    },
                )
                resp = await self.to_device(done_message, sas.transaction_id)
                if isinstance(resp, nio.ToDeviceError):
                    self.session.send_gateway_message(f"'done' failed with {resp}")

            elif yn.lower() == "n":  # no, don't match, reject
                resp = await self.cancel_key_verification(
                    event.transaction_id, reject=True
                )
                if isinstance(resp, nio.ToDeviceError):
                    self.session.send_gateway_message(
                        f"cancel_key_verification failed with {resp}"
                    )
            else:  # C or anything for cancel
                self.session.send_gateway_message(
                    "Cancelled by user! Verification will be cancelled."
                )
                resp = await self.cancel_key_verification(
                    event.transaction_id, reject=False
                )
                if isinstance(resp, nio.ToDeviceError):
                    self.session.send_gateway_message(
                        f"cancel_key_verification failed with {resp}"
                    )

        elif isinstance(event, nio.KeyVerificationMac):  # third step
            sas = self.key_verifications.get(event.transaction_id)

            if sas is None:
                self.session.send_gateway_message(f"transaction_id could not be found")
                return

            try:
                todevice_msg = sas.get_mac()
            except nio.LocalProtocolError as e:
                # e.g. it might have been cancelled by ourselves
                self.session.send_gateway_message(
                    f"Cancelled or protocol error: Reason: {e}.\n"
                    f"Verification with {event.sender} not concluded. "
                    "Try again?"
                )
            else:
                resp = await self.to_device(todevice_msg)
                if isinstance(resp, nio.ToDeviceError):
                    self.session.send_gateway_message(f"to_device failed with {resp}")
        elif event.source.get("type") == "m.key.verification.done":
            # Final step, other device acknowledges verification success.
            txid = content.get("transaction_id")
            sas = self.key_verifications[txid]

            self.session.send_gateway_message(
                f"sas.we_started_it = {sas.we_started_it}\n"
                f"sas.sas_accepted = {sas.sas_accepted}\n"
                f"sas.canceled = {sas.canceled}\n"
                f"sas.timed_out = {sas.timed_out}\n"
                f"sas.verified = {sas.verified}\n"
                f"sas.verified_devices = {sas.verified_devices}\n"
            )
            self.session.send_gateway_message("Emoji verification was successful!")
        else:
            self.session.send_gateway_message(
                f"Received unexpected event type {type(event)}. "
                f"Event is {event}. Event will be ignored."
            )
