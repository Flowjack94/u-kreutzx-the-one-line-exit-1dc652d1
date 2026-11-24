#!/usr/bin/env python3
"""The One-Line Exit - make.fun entry generator.

Writes one funny one-line resignation letter to /output/entry.txt.
Pure stdlib, deterministic. Gate: UTF-8 text, 1-140 chars, not only
whitespace, exactly one line.
"""

import hashlib
import os
import sys

ENTRY = (
    "Dear team, I hereby resign: the printer has jammed for the last "
    "time, and I refuse to spend another day in a relationship this "
    "one-sided."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry meets the gate: one line, 1-140 chars, real text."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Reject anything the gate's UTF-8 scorer would choke on: control
    # characters (other than none here, since newlines are already out),
    # the Unicode replacement character, and lone surrogates.
    for ch in text:
        code = ord(ch)
        if code < 0x20 or code == 0x7F:
            raise ValueError("entry contains control character U+%04X" % code)
        if ch == "\ufffd":
            raise ValueError("entry contains U+FFFD replacement character")
        if 0xD800 <= code <= 0xDFFF:
            raise ValueError("entry contains lone surrogate U+%04X" % code)
    # Encoding must round-trip cleanly (catches lone surrogates too).
    text.encode("utf-8")
    return True


def main():
    validate_entry(ENTRY)
    data = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and verify.
    with open(OUTPUT_PATH, "rb") as f:
        read_back = f.read()
    if read_back != data:
        print("ERROR: read-back bytes differ from written bytes", file=sys.stderr)
        sys.exit(1)
    text = read_back.decode("utf-8")  # raises on invalid UTF-8
    validate_entry(text)
    digest = hashlib.sha256(read_back).hexdigest()

    print("Entry: %s" % text)
    print("Chars: %d" % len(text))
    print("Bytes: %d" % len(read_back))
    print("SHA256: %s" % digest)
    print("OK")


if __name__ == "__main__":
    main()
