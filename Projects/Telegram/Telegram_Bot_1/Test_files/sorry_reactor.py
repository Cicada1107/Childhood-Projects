#sorry replier for the telegram_bot_1


from telethon import TelegramClient, events
import re, asyncio
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']

client = TelegramClient("Arijit Dubey", api_id, api_hash)



@client.on(events.NewMessage(pattern = r"(?i).*(sorry)\s*"), from_users = "Shivansh Kashyap", outgoing = False)
async def replier(event):
    user = await event.get_sender()
    dad = re.match(r".*(I'm|I am|My name is|i'm|i am|my name is|Me is)\s+.*", event.raw_text, re.IGNORECASE)
    if not dad:
        await event.reply("Oh ok np")
        
client.start()
client.run_until_disconnected()

