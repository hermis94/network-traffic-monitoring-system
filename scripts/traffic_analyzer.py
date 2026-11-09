"""Analyse a packet capture file and report the protocol distribution and top conversations."""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

from scapy.all import PcapReader


def summarize_pcap(pcap_path: str | Path, top_n: int = 10) -> dict:
    path = Path(pcap_path)
    if not path.exists():
        raise FileNotFoundError(f"PCAP file not found: {path}")

    protocol_counts: collections.Counter[str] = collections.Counter()
    conversations: collections.Counter[str] = collections.Counter()

    with PcapReader(str(path)) as packets:
        for packet in packets:
            if packet.haslayer("IP"):
                src = packet["IP"].src
                dst = packet["IP"].dst
                conversations[f"{src}->{dst}"] += 1

            layer = packet.lastlayer()
            if layer is None:
                protocol_counts["UNKNOWN"] += 1
            else:
                protocol_counts[layer.__class__.__name__] += 1

    summary = {
        "pcap_file": str(path),
        "packet_count": sum(protocol_counts.values()),
        "protocol_counts": dict(sorted(protocol_counts.items(), key=lambda item: (-item[1], item[0]))),
        "top_conversations": dict(
            sorted(conversations.items(), key=lambda item: (-item[1], item[0]))[:top_n]
        ),
    }
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a packet capture file.")
    parser.add_argument("pcap", type=Path, help="Path to the PCAP file to analyse")
    parser.add_argument("--top-n", type=int, default=10, help="Number of top conversations to display")
    parser.add_argument("--output", type=Path, default=None, help="Optional output JSON file")
    args = parser.parse_args()

    summary = summarize_pcap(args.pcap, args.top_n)
    printed = json.dumps(summary, indent=2, sort_keys=True)
    print(printed)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(printed + "\n", encoding="utf-8")
        print(f"\nSaved JSON summary to {args.output}")
