#learning the instinance function at last

import asyncio, tqdm, matplotlib
from telethon import TelegramClient, events
from configparser import ConfigParser
from time import sleep

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Arijit Dubey", api_id, api_hash)

#user = client.get_dialogs('Shivansh Kashyap')

for dialog in client.iter_dialogs():
    print(dialog.name, 'has ID', dialog.id)



while True:
    if isinstance(user.status, UserStatusOffline):
        if contact.offline:
            print("Uhm what is this code *_*")



client.start()
client.run_until_disconnected()
