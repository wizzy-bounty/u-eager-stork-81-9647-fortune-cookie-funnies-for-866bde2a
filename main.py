import os
from pathlib import Path

ENTRY = "Your TODO from March will soon introduce itself as legacy architecture."
OUTPUT_FILENAME = "entry.txt"


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / OUTPUT_FILENAME).write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
