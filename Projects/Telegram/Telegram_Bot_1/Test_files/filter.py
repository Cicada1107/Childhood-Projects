from telethon import TelegramClient, events
import re
import asyncio
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Arijit Dubey", api_id, api_hash)



@client.on(events.NewMessage(pattern = r"(?i).*(fuck|hell|ass|sex|fook|faggot|chutiya|bsd|bhosri|bhosdi|wtf|tf).*"))
async def mod(event):
    await asyncio.sleep(25)
    await event.delete()

client.start()
client.run_until_disconnected()
