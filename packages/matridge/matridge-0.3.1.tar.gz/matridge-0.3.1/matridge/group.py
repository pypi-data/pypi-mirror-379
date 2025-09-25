import typing

import nio
from slidge.group import LegacyBookmarks, LegacyMUC, LegacyParticipant, MucType
from slidge.util.types import HoleBound
from slixmpp.exceptions import XMPPError

from . import config
from .util import MatrixMixin, server_timestamp_to_datetime

if typing.TYPE_CHECKING:
    from .session import Session


class Participant(MatrixMixin, LegacyParticipant):
    session: "Session"
    muc: "MUC"

    def set_affiliation_from_power_level(self, power_level: int) -> None:
        if power_level == 100:
            self.affiliation = "owner"
            self.role = "moderator"
        elif power_level >= 50:
            self.affiliation = "admin"
            self.role = "moderator"
        else:
            self.affiliation = "member"
            self.role = "participant"


class Bookmarks(LegacyBookmarks):
    session: "Session"

    async def fill(self):
        self.log.debug("Filling rooms")
        for room in self.session.matrix.rooms:
            try:
                await self.by_legacy_id(room)
            except XMPPError as e:
                self.log.debug(
                    "%s is not a group chat or trouble getting it: %r", room, e
                )


class MUC(LegacyMUC[str, str, Participant, str]):
    session: "Session"
    type = MucType.CHANNEL_NON_ANONYMOUS

    async def get_room(self):
        try:
            return self.session.matrix.rooms[self.legacy_id]
        except KeyError:
            raise XMPPError("item-not-found", f"No room named {self.legacy_id}")

    async def get_message(self, msg_id: str) -> typing.Optional[nio.Event]:
        return await self.session.matrix.get_event(self.legacy_id, msg_id)

    async def update_info(self):
        room = await self.get_room()

        if new := room.replacement_room:
            localpart = await self.session.bookmarks.legacy_id_to_jid_username(new)
            raise XMPPError(
                "redirect", f"xmpp:{localpart}@{self.xmpp.boundjid.bare}?join"
            )
        self.log.debug("Children: %s", room.children)
        if room.children:
            raise XMPPError("bad-request", "This is not a real room but a 'space'")

        self.user_nick = room.user_name(self.session.matrix.user_id)

        self.log.debug("User nick: %s", self.user_nick)
        self.name = room.display_name
        self.log.debug("Avatar: %s", room.room_avatar_url)
        self.n_participants = room.member_count
        self.subject = room.topic

        if room.room_avatar_url:
            self.avatar = await self.session.matrix.mxc_to_http(room.room_avatar_url)

        elif room.member_count == 2:
            # if 1:1 set room avatar to other users's avatar
            for user_id, user in list(room.users.items()):
                if user_id == self.session.matrix.user_id:
                    continue
                if user.avatar_url is None:
                    break
                self.avatar = await self.session.matrix.mxc_to_http(user.avatar_url)
                break

    async def fill_participants(self):
        room = await self.get_room()
        if not room.members_synced:
            resp = await self.session.matrix.joined_members(self.legacy_id)
            if isinstance(resp, nio.JoinedMembersResponse):
                self.log.debug(
                    "Joined members response: %s participants", len(resp.members)
                )
            else:
                self.log.debug("Joined members error: %s", resp)

        power_levels = room.power_levels.users
        i = 0

        for user_id, user in list(room.users.items()):
            power_level = power_levels.get(user_id, 0)
            if power_level < 50 and i > config.MAX_PARTICIPANTS_FETCH:
                continue
            try:
                p = await self.get_participant_by_legacy_id(user.user_id)
            except XMPPError:
                continue
            p.set_affiliation_from_power_level(power_level)
            if power_level < 50:
                i += 1
            yield p

    async def backfill(
        self,
        after: HoleBound | None = None,
        before: HoleBound | None = None,
    ):
        after_date = None if after is None else after.timestamp
        before_date = None if before is None else before.timestamp
        async for event in self.session.matrix.fetch_history(
            self.legacy_id,
            config.MAX_HISTORY_FETCH,
        ):
            if not isinstance(event, nio.RoomMessage):
                self.log.debug("Not back-filling with %s", type(event))
            when = server_timestamp_to_datetime(event)
            if after_date is not None and when <= after_date:
                continue
            if before_date is not None and when >= before_date:
                continue
            try:
                participant = await self.session.matrix.get_participant(
                    await self.get_room(), event
                )
            except XMPPError as e:
                # maybe deleted profiles?
                self.log.debug(
                    "Something is wrong with participant %s, falling back to using matrix ID as nickname: %s",
                    event.sender,
                    e,
                )
                participant = await self.get_participant(event.sender)

            await participant.send_matrix_message(event, archive_only=True)

            # FIXME: this breaks everything, probably because of parallel calls
            #        to sync()
            # if isinstance(event, nio.UnknownEvent) and event.type == "m.reaction":
            #     await self.session.matrix.on_reaction(
            #         await self.get_room(), event, when=when, archive_only=True
            #     )
            #     continue
