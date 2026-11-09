#learning the instinance function at last


'''
The methods that seem to have some potential are:
1. iter_dialogs for chats that are already initiated
2. client.get_entity
'''

import asyncio, tqdm, re, csv
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


client = TelegramClient("Tass_1", api_id, api_hash)

'''
#This code is very very good for clearing your concept on the topic of entities and updates.

@client.on(events.NewMessage)
async def test(msg):
    chat = await msg.get_chat()
    sender = await msg.get_sender()
    sub = await client.get_entity('+91 72781 23456')
    print(chat, sender, sub, sep = "\n************************************\n")
    print(chat.username, sender.username, sub.username, sep = "\n************************************\n")
    print(sub.status)
    if isinstance(sub.status, types.UserStatusOnline):
        print(Gotcha)
'''

#Finally did it
#This can be now succefully converted or extracted to form a command or can be adapted to a non event based set up which does not require a command to be set.
@client.on(events.NewMessage(pattern = r"(?i)^!deploy.*", outgoing = True))
async def test(msg):
    await msg.delete()
    sub = await client.get_entity('+919903292350')
    print("Monitor initiated\nTime: {}".format(datetime.now().strftime("%H:%M:%S")))
    while True:
        online = isinstance(sub.status, types.UserStatusOnline)
        if online:
            online_time = datetime.now().strftime("%H:%M:%S")
            print("**User online**\nTime: {}".format(online_time))
            while online:
                off_time = datetime.now().strftime("%H:%M:%S")
            duration = off_time - online_time
            with open('rec.csv', "a") as file:
                writer = csv.writer(file, delimiter = ',')
                writer.writerow([sub.username, online_time, duration])


client.start()
client.run_until_disconnected()
