#Tassabi_online_tracking
#WOrking. But only works once for now I guess.

import asyncio, tqdm, re, csv, ast, shlex
from winsound import Beep
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

hit_list = {}
n = int(input("Please enter the number of people to message: "))
for i in range(n):
    s = i+1#More optimised than performing the operation twice.
    num = input("Enter the full phone number(with code) of person {}: ".format(s))
    m = input("Enter the message you want to send to person {}: ".format(s))
    msg = ast.literal_eval(shlex.quote(m))  #just internet, for recognising escape sequences in input
    hit_list.update({num: msg})

print('==========BOT DEPLOYED=========\nTime of initiation: {}'.format(datetime.now().strftime('%H:%M:%S')))

@client.on(events.UserUpdate(chats = list(hit_list.keys())))
async def online(event):
    if event.online:
        online_time = datetime.now().strftime('%H:%M:%S')
        sub_id = event.user_id
        sub = await client.get_entity(sub_id)      #await event.get_user() not using this as works only on me. Probable reasons: the spaces in phone numbers entered by the user.
        sub_username = sub.username
        num = '+' + sub.phone
        await client.send_message(num, hit_list[num])#sub_username
        print("Message sent succesfully at {}".format(online_time))
        Beep(3500, 100)
        #sleep(50)

client.start()
client.run_until_disconnected()
