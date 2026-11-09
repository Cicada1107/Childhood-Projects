#link_purge

'''
Purges all the links in a given chat'''

from telethon import TelegramClient, events
from configparser import ConfigParser
import re

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']

client = TelegramClient("Arijit Dubey", api_id, api_hash)


@client.on(events.NewMessage(pattern = r"(?i)^!lpurge"))
async def sos(event):
    """Deletes all messages containing youtube links in a chat"""
    await event.delete()
    chat = event.chat_id
    msgs = await client.get_messages(chat, 700)
    for msg in msgs:
        match = re.search(r".*(https://|http://).+", msg.raw_text)
        user = await msg.get_sender()
        if user.username != "Momentii1107" and match:
            #print(msg.raw_text)
            await msg.delete()
    print("Procedure completed succesfully")

client.start()
client.run_until_disconnected()
