# Hermis Makawa - Network Traffic Monitoring System

**Student:** Hermis Makawa  
**Serial no.:** 15  
**Project title:** Network Traffic Monitoring System

## Project brief
This project is about looking at real network traffic in a safe lab setup and identifying what is normal, what is unusual, and what might be worth flagging as a security concern. I used Wireshark-style analysis as the core of the work, because that is one of the clearest ways to see how devices are talking to each other on the network.

The focus is not to guess wildly from a single packet capture. It is to examine the traffic carefully, note protocols and ports, and then explain what stands out in a concise and evidence-based way.

## What I wanted to achieve

- Capture a short sample of authorised network activity.
- Inspect information such as protocol, source, destination, and port.
- Identify normal services and anything that looks suspicious or unusual.
- Summarise the findings in a readable security report.
- Use the project as evidence in the final portfolio.

## Deliverables

- Packet capture or screenshot evidence
- A traffic-analysis script
- A short report with observations and recommendations

## Folder structure

- `scripts/capture_packets.py` — packet capture helper
- `scripts/traffic_analyzer.py` — summarises protocol and conversation data
- `scripts/summarize_traffic.py` — extracts a quick tshark summary
- `docs/traffic_analysis_report.md` — project report
- `docs/traffic_analysis_report_template.md` — evidence checklist
- `requirements.txt` — Python requirements for the analysis helper

## Example workflow

```bash
python -m pip install -r requirements.txt
python scripts/capture_packets.py
python scripts/traffic_analyzer.py capture.pcap
```

## Notes

This project is intentionally kept separate from the earlier fraud-detection work in the workspace, and it follows the assignment in COMPREHENSION-1_121908.pdf.
