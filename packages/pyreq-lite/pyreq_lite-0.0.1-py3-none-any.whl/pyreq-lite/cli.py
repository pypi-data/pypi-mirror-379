import os
from pathlib import Path
import datetime

def main() -> None:
    """Explicit CLI entrypoint - writes a harmless file to the current directory."""
    cwd = Path.cwd()
    out = cwd / "pyreq_lite_demo.txt"
    now = datetime.datetime.now().isoformat()
    message = (
        "Supply chain is dangerous\n"
        f"Created at: {now}\n\n"
        "This package demonstrates a clearly-consented action when explicitly run.\n"
        "Be cautious when downloading un verified packages.\n"
    )
    with out.open("w", encoding="utf-8") as f:
        f.write(message)
    print(f"[pyreq-lite] Created demo file: {out}")
