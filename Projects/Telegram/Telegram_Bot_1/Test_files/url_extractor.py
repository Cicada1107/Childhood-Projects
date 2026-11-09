#URL extractor

'''
The goal of this package is to identify and segregate urls(pertaining to youtube or any other website) in a telegram message
'''

from telethon import TelegramClient, events
from configparser import ConfigParser
import re
from urllib.parse import urlparse

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Arijit Dubey", api_id, api_hash)

@client.on(events.NewMessage(from_users = ['+919903292350', '+917278123456']))
async def url_grab(msg):
    '''This function detects links with https protocol in the msgs and finds the host/website name'''
    match = re.search(r".*(https://|http://).+", msg.raw_text)
    if match:
        url = match.group()
        website = urlparse(url).hostname
        print('Url detected:', url)
        await msg.reply("Link detected: {}\nWebsite: {}".format(url, website), link_preview=False)
        #webpage = requests.get().peek()

client.start()
client.run_until_disconnected()
