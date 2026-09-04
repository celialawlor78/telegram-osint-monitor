import asyncio
import os

import pandas as pd
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
SESSION_NAME = "osint_scraper_session"

CHANNELS = ["@rybar", "@baza"]
KEYWORDS = ["санкции", "граница", "бпла", "кибератака", "казахстан"]


async def scrape_channels():
    data = []

    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()

    try:
        for channel in CHANNELS:
            print(f"Scraping {channel}...")

            try:
                async for message in client.iter_messages(channel, limit=100):
                    if not message.text:
                        continue

                    text_lower = message.text.lower()
                    matched_words = [
                        word for word in KEYWORDS if word in text_lower
                    ]

                    if matched_words:
                        data.append(
                            {
                                "channel": channel,
                                "date_utc": message.date,
                                "message_id": message.id,
                                "text": message.text,
                                "matched_keywords": ", ".join(matched_words),
                            }
                        )
            except Exception as error:
                print(f"Could not scrape {channel}: {error}")

    finally:
        await client.disconnect()

    df = pd.DataFrame(data)
    df.to_csv("telegram_osint_results.csv", index=False, encoding="utf-8-sig")
    print(f"Saved {len(df)} matching messages.")


if __name__ == "__main__":
    asyncio.run(scrape_channels())