"""Generate a tshark protocol hierarchy summary for a captured PCAP file."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise a PCAP file using tshark's protocol hierarchy view.")
    parser.add_argument("pcap", type=Path, help="Path to the capture file")
    parser.add_argument("--output", type=Path, default=None, help="Optional file to save the summary output")
    args = parser.parse_args()

    cmd = ["tshark", "-r", str(args.pcap), "-q", "-z", "io,phs"]
    print("Running tshark protocol summary...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print("tshark is not installed. Install Wireshark or use another authorised packet analysis tool.")
        raise SystemExit(1)
    except subprocess.CalledProcessError as exc:
        print(f"Summary failed with exit code {exc.returncode}")
        if exc.stderr:
            print(exc.stderr)
        raise SystemExit(1)

    output = result.stdout
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print(f"Summary saved to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
