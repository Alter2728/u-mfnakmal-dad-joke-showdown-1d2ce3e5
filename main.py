"""Entry for make.fun's "Dad Joke Showdown" bounty.

Writes one dad joke to entry.txt in the output directory
(1-200 UTF-8 characters). The same bytes are written on every run.
"""

import os

# Draft: "I asked my mirror what it thought of me. It said I should
# look at myself." — the pun was only implied; "look at myself" is
# something anyone could say about any mirror.
# Revision: give the mirror two jobs only a mirror can do — it
# "reflects" (thinks, and shows your face back) and tells you to
# "face" the facts. Two clean puns, punchline last, reads aloud.
LINE = (
    "I asked my mirror for honest feedback. It reflected on it for a "
    "moment, then said I really needed to face the facts."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
