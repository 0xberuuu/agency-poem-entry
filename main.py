"""Write one poem about agency to entry.txt.

The poem is fixed text: no randomness, no network, no clock. Every run
writes exactly the same bytes.
"""

import os

POEM = """It is not the doing.
The doing is cheap now:
a thousand tireless hands
waiting for one word.

It is the pause before the word,
the hand above the switch,
the one who decides
what the light is for.

I lend you my errands,
my inbox, my keys.
You carry them further
than my arms ever reached.

But the wanting stays here —
the yes, the no,
the small stubborn weight
of choosing at all.

That is the one thing
I cannot hand over:
my hand on the switch,
the dark, and the choice.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
