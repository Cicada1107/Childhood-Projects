#Learning 3
#This can now keep a system that tells me who comes online and when

import asyncio, tqdm, re, csv, winsound
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


client = TelegramClient("oof", api_id, api_hash)

file = open('online_log.csv', 'a+', newline='')
writer = csv.writer(file, delimiter = '|')
writer.writerow(['Name', 'Online Time', 'Duration', 'Date'])
file.close()


#I have close to no idea on how to use this function and this is pretty much all based on calculated guesswork.
#Turns out this actually works after a bit of modification lol
@client.on(events.UserUpdate)
async def online(event):
    print('***Monitor Initiated***\nTime of initiation: {}'.format(datetime.now().strftime('%H:%M:%S')))
    if event.online:
        current_date = date.today()
        online_time = datetime.now().strftime('%H:%M:%S')
        sub = event.user_id
        sub_2 = await client.get_entity(sub)
        sub_username = sub_2.username
        print("{} just came online at {}".format(sub_username, online_time))
        while event.online:
            offline_time = datetime.now().strftime('%H:%M:%S')
        duration = offline_time - online_time
        with open('online_log.csv', 'a+', newline='') as file:
              writer = csv.writer(file, delimiter = '|')
              writer.writerow([sub_username, online_time, duration, current_date])
              file.close()



client.start()
client.run_until_disconnected()
