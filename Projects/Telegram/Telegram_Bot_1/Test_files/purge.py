#Version 2
#Ok so how am I supposed to get the username or Id or any such information about the chat the command is sent to?

from telethon import TelegramClient, events
import re
import time
import asyncio
import os
from configparser import ConfigParser


#using condfig parser to migtrate telegram info
config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Arijit Dubey", api_id, api_hash)


@client.on(events.NewMessage(pattern = r"(?i)^!purge"))
async def purge(event):
    #target = client.get_sender(event.caht)
    try:
        n = int(event.raw_text.split()[1])
        chat = event.chat_id
        #[await msg.delete() async for msg in client.iter_messages(event.chat_id, limit = n+1)] #For slow delete
        msgs = await client.get_messages(chat, n+1)
        await client.delete_messages(chat, msgs)
        await event.delete()
    except IndexError:
        await event.reply("**No. of messages to delete not mentioned!**\nFormat: `!purge <No. of messages to purge>`")


client.start()
client.run_until_disconnected()
