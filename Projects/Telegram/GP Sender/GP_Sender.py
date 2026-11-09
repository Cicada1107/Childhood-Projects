#Program to send question marks in Arithmetic progression to shivansh in time intervals that are also in AP

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

x = 0
while x < 50:
    x += 1
    payload = 'Br' + x**2*'o'

    with client:
        client.loop.run_until_complete(client.send_message(entity = '+919903292350', message = payload))
    sleep(x**0.5)

        
