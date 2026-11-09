#Tassabi_online_tracking

import asyncio, tqdm, re, pprint
from datetime import date, datetime
from telethon import TelegramClient, events, types
from configparser import ConfigParser
from time import sleep

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Tass_x_rec", api_id, api_hash)


@client.on(events.NewMessage(pattern = r"(?i).*jej"))#, from_users = '+91 99032 92350'))
async def spanishize(msg):
    user = await msg.get_sender()
    if user.username == "gamerXgo_1974":
       await msg.delete()
    else:
       await msg.reply('🤌')

@client.on(events.NewMessage(from_users = '+91 99032 92350'))
async def deleter(msg):
    if '🤌' in msg.raw_text:
        await msg.delete()

@client.on(events.NewMessage(from_users = '+91 99032 92350'))
async def last_ditched_attempt(msg):
    msg.reply('🤌')


client.start()
client.run_until_disconnected()
