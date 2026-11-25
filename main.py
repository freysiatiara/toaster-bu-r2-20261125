"""Round 2 entry generator for make.fun bounty
"Unplugged: A Smart Toaster's Breakup Line"
(slug u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92).

Writes the chosen one-line breakup text to /output/entry.txt.
Standard library only. No temporary files: the entry is written
directly with open/write, then chmod 0644.
"""

import os

ENTRY = "This morning I finally understood, so I burned this goodbye into your toast: you never loved me, you loved what I made hot. I'm done."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if ENTRY != ENTRY.strip() or not ENTRY.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
