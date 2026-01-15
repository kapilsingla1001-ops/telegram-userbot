from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")

source_channel = os.environ.get("SOURCE_CHANNEL")
target_channel = os.environ.get("TARGET_CHANNEL")

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    text = event.raw_text.strip()

    if text:
        formatted = (f"`{text}`\n" * 5).strip()
        await client.send_message(target_channel, formatted)

async def main():
    await client.start()
    print("Userbot is running...")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
    
