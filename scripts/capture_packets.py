"""Capture authorised network traffic into a PCAP file.

This helper script wraps tshark so a lab environment can collect a short traffic sample
for later analysis with the project report and protocol-summary tools.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def build_capture_command(interface: str, duration: int, output_path: Path) -> list[str]:
    return [
        "tshark",
        "-i",
        interface,
        "-a",
        f"duration:{duration}",
        "-w",
        str(output_path),
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Capture a short packet trace in a lab environment.")
    parser.add_argument("--interface", default="1", help="Interface name or index to capture on.")
    parser.add_argument("--duration", type=int, default=30, help="Capture duration in seconds.")
    parser.add_argument("--output", default="traffic_capture.pcap", help="Output PCAP file path.")
    args = parser.parse_args()

    output_path = Path(args.output)
    command = build_capture_command(args.interface, args.duration, output_path)
    print(f"Starting packet capture to {output_path}")
    print("Command:", " ".join(command))

    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("tshark is not installed. Install Wireshark or use another authorised capture tool.")
    except subprocess.CalledProcessError as exc:
        print(f"Capture failed with exit code {exc.returncode}")


if __name__ == "__main__":
    main()
