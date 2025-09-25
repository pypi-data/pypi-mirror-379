MAX_HISTORY_FETCH = 100
MAX_HISTORY_FETCH__DOC = (
    "Number of events to fetch to back-fill MUC history before slidge starts up."
)

MAX_PARTICIPANTS_FETCH = 10
MAX_PARTICIPANTS_FETCH__DOC = (
    "Number of participants to fetch when joining a group. "
    "Higher values will make joining slower, and participants will appear when "
    "they speak or if they spoke in the back-filled events. "
    "Participants with power levels > 50 (ie, admins) will be fetched."
)

NIO_VERBOSE = False
NIO_VERBOSE__DOC = (
    "Set this to True to respect the global log level from the matrix lib. "
    "It's REALLY verbose, so the default is to use WARNING."
)

PARSE_MESSAGE_STYLING = True
PARSE_MESSAGE_STYLING__DOC = """
Convert Message Styling (XEP-0393) message bodies to Matrix custom HTML.
Supported markup:
_underline_
*bold*
~strikethrough~
`code span`
```code block```
>quote
||spoiler
\\_escape style_
"""

REACTION_CACHE_SIZE = 10000
REACTION_CACHE_SIZE__DOC = "Emoji reaction cache size, in number of messages"
