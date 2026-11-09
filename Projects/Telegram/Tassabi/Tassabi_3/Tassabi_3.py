#Tassabi_3
#This one is event based and notifies you when any user comes online and
#can be modified for targetting a single user

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


client = TelegramClient("Tass_x_rec", api_id, api_hash)

file = open('online_log.csv', 'a+', newline='')
writer = csv.writer(file, delimiter = '|')
writer.writerow(['Name', 'Online Time', 'Duration', 'Date'])
file.close()


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
