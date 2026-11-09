#Telethon api learning
#This is following the official documentation of telethon library
#https://docs.telethon.dev/en/latest/

'''
from telethon.sync import TelegramClient, events
#from telethon.tl.functions import GetDialogsRequest
#from telethon.tl.types import InputPeerEmpty
#from telethon.tl.types import InputPeerUser
#from telethon.errors.rpcerrorlist import PeerFloodError
#import time, os, sys, csv, random
import asyncio
'''

from telethon import TelegramClient

# Use your own values from my.telegram.org
name = "Arijit Dubey"
api_id = "14630422"
api_hash = "d8d23219b71c70495455b9598d0280af"
phone = "+919433374114"
username = "Momentii1107"

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('Arijit Dubey', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))
