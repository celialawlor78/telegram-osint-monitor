# telegram-osint-monitor
Python tools for monitoring Eurasian political-risk signals through public Telegram

## Tools

- `monitor.py` reviews recent posts from selected public Russian-language Telegram channels and flags user-defined keywords.
- `trade_tracker.py` retrieves UN Comtrade data to identify trade-anomaly candidates for further research.

## Purpose

This project combines Russian-language OSINT, Python, and structured analytical methods to support research on Eurasian political risk, hybrid threats, and sanctions-evasion indicators.

## Important limitation

The tools identify leads for further investigation. A keyword match or trade spike does not establish intent, sanctions evasion, or attribution.

## Setup

```bash
pip install -r requirements.txt
