#Tassabi_online_tracking

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


'''
file = open('online_log.csv', 'a+', newline='')
writer = csv.DictWriter(file, delimiter = '|', fieldnames = ['Name', 'Online Time', 'Duration', 'Date'])
writer.writeheader()
file.close()
'''


n = int(input("Please enter the number of contacts you want to trace: "))
target_list = []
for i in range(n):
    num = input("Please enter the full phone number(with code) of the contact you want to track: ")
    #target = client.get_entity(num)
    target_list.append(num)

#develop a method to identify and display the list of full names of the targets so the user can atleast know if he typed in the right number.

print('===============MONITOR(s) INITIATED===============\nTime of initiation: {}'.format(datetime.now().strftime('%H:%M:%S')))


@client.on(events.UserUpdate(chats = target_list))
async def online_tracker(event):
    if event.online:
        winsound.Beep(2000, 400)
        user = await event.get_user()
        target_username = user.username
        current_date = date.today()
        online_time = datetime.now().strftime('%H:%M:%S')
        print("{} just came online at {}".format(target_username, online_time))
        online_time = datetime.now().strftime('%H:%M:%S')
        duration = event.until
        print("Duration:", duration)
        with open('online_log.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter = '|')
            writer.writerow([target_username, online_time, duration, current_date])
            file.close()


client.start()
client.run_until_disconnected()
