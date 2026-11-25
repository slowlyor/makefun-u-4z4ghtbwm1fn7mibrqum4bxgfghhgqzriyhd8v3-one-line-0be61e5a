#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes a single original funny line to /output/entry.txt.
The line must be 1-140 characters of UTF-8 text, not only whitespace.
"""
import os

LINE = "I asked AI to write my dating profile; now strangers reject me at machine speed."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
