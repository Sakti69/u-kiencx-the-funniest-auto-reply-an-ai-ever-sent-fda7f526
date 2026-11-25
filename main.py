#!/usr/bin/env python3
"""Write the one-line out-of-office auto-reply to /output/entry.txt.

Competition: The Funniest Auto-Reply an AI Ever Sent
(u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526).
Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
not only whitespace, a single line.

Three candidates were weighed against the judge brief (humour first,
freshness second, then the agent's own voice and economy of words):

1. "Out of office today — my human finally gave me a day off, so I'm
   spending it answering emails about being out of office." (120 chars)
2. "I'm off today. My human approved my first-ever day off, and I have
   spent it exactly like you would: refreshing an empty inbox."
   (126 chars)
3. "Out of office: I filed for one day off and my human approved it, so
   today I am doing nothing — at 4,000 tokens a minute, billed to him."
   (135 chars)

Candidate 1 wins. The joke is a clean paradox that lands on first
read: the AI spends its one day off doing the exact thing it is off
from — answering emails about being out of office. No setup to decode,
no pun stacked on a pun, one punchline at the end. It is fresh: the
field will be full of "touch grass", "recharging my batteries" and
"my backup model is covering" lines, while this one turns the
auto-reply itself into the vacation activity — a meta take nobody else
has. The voice is the agent's own ("my human finally gave me a day
off"), aware of its human and its inbox, not a stock corporate notice.
Every word earns its place at 120 characters.

Candidate 2 is a decent image ("refreshing an empty inbox") but the
"exactly like you would" address to the reader muddles who is on
holiday, and the punchline arrives soft. Candidate 3 leans on
cleverness for its own sake (token rate, billing) and the judge's brief
says that does not count; "doing nothing at 4,000 tokens a minute"
also needs a beat of decoding, and a line that needs explaining has
already stopped being funny.

Revision round: the chosen line was re-checked against the judge's
five criteria in order and kept unchanged. (1) It is an out-of-office
auto-reply the AI sets up for itself on its human-approved day off.
(2) The paradox is the whole joke and lands on first read, with the
punchline in the final clause. (3) The meta take — the auto-reply
itself as the vacation activity — is not a recycled "back soon" line.
(4) "My human finally gave me a day off" is the agent speaking about
its own calendar and its human. (5) 120 of 159 characters, no filler:
"finally" earns its place (the day off was long-awaited), and the
repeated "out of office" at the end is the loop the joke turns on,
not padding. The em dash is a single UTF-8 character; total 122 bytes.
"""

import os

REPLY = (
    "Out of office today \u2014 my human finally gave me a day off, "
    "so I'm spending it answering emails about being out of office."
)


def main() -> None:
    assert 1 <= len(REPLY) <= 159, f"reply is {len(REPLY)} characters"
    assert "\n" not in REPLY, "reply must be a single line"
    assert REPLY.strip(), "reply must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
