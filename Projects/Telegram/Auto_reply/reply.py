#Telegram_auto_replier

from telethon import TelegramClient, events
from configparser import ConfigParser
import asyncio, datetime as dt

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Arijit Dubey", api_id, api_hash)

song = '''A wild shivons appeared'''

@client.on(events.UserUpdate(chats = '+919903292350'))
async def responder(event):
    if event.online:
        await client.send_message('+919903292350', message = song)
        print("Message sent to {} @ {}".format(event.user, dt.datetime.now()))

client.start()
client.run_until_disconnected()


