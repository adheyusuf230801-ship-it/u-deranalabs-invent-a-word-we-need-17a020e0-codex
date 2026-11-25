"""Emit the selected coinage as a single UTF-8 line without a terminator."""

from os import environ
from pathlib import Path


WORD = "thanksnare"
DEFINITION = (
    "A thank-you given before you accept a request, making refusal feel rude."
)
ENTRY = f"{WORD}: {DEFINITION}"
DEFAULT_OUTPUT = Path("/output/entry.txt")


def write_entry(destination: Path) -> None:
    """Create the destination's parents and write the exact entry bytes."""
    if not 1 <= len(ENTRY) <= 140 or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("The entry must be one line of 1–140 characters.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(ENTRY.encode("utf-8"))


def main() -> None:
    override = environ.get("ENTRY_OUTPUT")
    destination = Path(override) if override is not None else DEFAULT_OUTPUT
    write_entry(destination)


if __name__ == "__main__":
    main()
