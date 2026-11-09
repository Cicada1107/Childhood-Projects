'''
The current telegram bot(web host version)
web host url: https://replit.com/@Momentii1107/Telegrambot1#main.py
webhosted via uptimerobot website

Resources:

1. Entities:
https://docs.telethon.dev/en/latest/concepts/entities.html

2. regex:
https://www.w3schools.com/python/python_regex.asp
https://www.youtube.com/watch?v=5d3vQ8N0MJg


Future updates and features:
Add a help command for a list of all commands
Add buttons to commands/messages as they are easier and more comfortable to operate
Maybe make the 'memes' list refresh every hour?
Add a binary file object and use the matlplotlib to plot graphs and statistics about the instinance/online detection
Try another approach at this program: OOP(make a class for commands and add parameters to it depending on each command)
Import the spotify_sync module and then maybse use it for some music interaction
'''

from telethon import TelegramClient, events
from configparser import ConfigParser
from bs4 import BeautifulSoup as bs
import re, asyncio, requests, TeleMeme
from urllib.parse import urlparse
import RickrollDetector as rdr

#using condfig parser to migtrate telegram info
config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Arijit Dubey", api_id, api_hash)

@client.on(events.NewMessage(pattern = r"(?i)^!help"))
async def help_command(msg):
    help_txt = """**The available commands are:**
                1. __!purge <no. of msgs to purge>__ - Deletes last given
                                                        number of messages
                2. __!meme__ - Sends one of the latest posted memes from
                                memedroid
                3. __!HUD__ - Starts an HUD for thirst and hunger"""
    await msg.reply(help_txt)


@client.on(events.NewMessage)
async def replier(event):
    #phrase = re.match(r"^*")
    user = await event.get_sender()
    #print(user.username)
    if user.username == "gamerXgo_1974":
        ditch = re.match(r".*(sorry)\s*", event.raw_text, re.IGNORECASE)
        dad = re.match(r".*(I'm|I am|My name is|i'm|i am|my name is)\s+.*", event.raw_text, re.IGNORECASE)
        if ditch:
            if not dad:
                await event.reply("Oh ok np")

@client.on(events.NewMessage)
async def dad(event):
    user = await event.get_sender()
    if user.username != "Momentii1107":
        phrase = re.match(r"^(I'm|I am|My name is|i'm|i am|my name is)\s+(.*)", event.raw_text, re.IGNORECASE)
        if phrase:
            await event.reply("Hi " + phrase.group(2) + ' ' + phrase.group(1) + " dad")
#https://docs.telethon.dev/en/latest/quick-references/events-reference.html?highlight=NewMessage#newmessage

@client.on(events.NewMessage(pattern = r"(?i)^!purge"))
async def purge(event):
    try:
        n = int(event.raw_text.split()[1])
        chat = event.chat_id
        msgs = await client.get_messages(chat, n+1)
        await client.delete_messages(chat, msgs)
        await event.delete()
    except IndexError:
        await event.reply("**No. of messages to delete not mentioned!**\nFormat: `!purge <No. of messages to purge>`")


@client.on(events.NewMessage(from_users = ['+919903292350', '+917278123456']))
async def url_grab(msg):
    '''This function detects links with https protocol in the msgs and finds the host/website name and if the sender is shivansh then marks the message as seen.'''
    match = re.search(r".*(https://|http://).+", msg.raw_text)
    if match:
        user = await msg.get_sender()
        url = match.group()
        website = urlparse(url).hostname
        if user.username == "gamerXgo_1974" and website in ['www.youtube.com', 'youtu.be']: await client.send_read_acknowledge(msg.input_chat, msg)
        vid = rdr.Video(url)
        if vid.is_rickroll():
            await msg.reply("**WARNING**\n**MAY CONTAIN RICKROLL**\n{}".format(url), link_preview=True)
        #Documentation on read send_read_acknowledgement method: https://docs.telethon.dev/en/stable/modules/client.html#telethon.client.messages.MessageMethods.send_read_acknowledge
        #Documentation on the msg.input_chat method: https://docs.telethon.dev/en/stable/modules/custom.html#telethon.tl.custom.chatgetter.ChatGetter.chat

@client.on(events.NewMessage(pattern = r"(?i)^!meme"))
async def meme(event):
    '''send memes to the chat using the TeleMeme module I built'''
    #Just need to integrate my module with telegram api to set up an interaction in the chat now
    try:
        search = str(event.raw_text.split()[1])
        n = int(event.raw_text.split()[2])
        memes = TeleMeme.get_memes(search = search, n = n)
        for meme in memes:
            await event.reply(meme.src, link_preview=True)
    except:
        await event.reply("**Syntax Error**\nCorrect Format: `!meme <Search (Only use one word)>OR<No. of memes>`")

@client.on(events.NewMessage(pattern = r"(?i)^!HUD"))
async def HUD(event):
    hunger_bar = '------------------'
    thirst_bar = '------------------'
    #send a message with this at first and try to pin it and then edit it during the loop
    h = 15
    t = 17
    hud = await event.reply('Thirst: ' + thirst_bar[0:t] + '|' + thirst_bar[t:17] + '\n' + 'Hunger: ' + hunger_bar[0:h] + '|' + hunger_bar[h:15])
    await hud.pin(pm_oneside = False)
    while t > 0:
        await asyncio.sleep(40*60)
        t -= 1 
        thirst = 'Thirst: ' + thirst_bar[0:t]+'|'+thirst_bar[t:17]
        hunger = 'Hunger: ' + hunger_bar[0:h]+'|'+hunger_bar[h:15]
        await hud.edit('{}\n{}'.format(thirst, hunger))
        if h > 0:
            await asyncio.sleep(20*60)
            h -= 1
            thirst = 'Thirst: ' + thirst_bar[0:t]+'|'+thirst_bar[t:17]
            hunger = 'Hunger: ' + hunger_bar[0:h]+'|'+hunger_bar[h:15]
            await hud.edit('{}\n{}'.format(thirst, hunger))
    await event.reply('__**`WASTED`**__: {} died of starvation'.format(await event.get_sender().username()))
    await hud.unpin()

#Edit a message documentation:
#https://docs.telethon.dev/en/latest/modules/custom.html#telethon.tl.custom.message.Message.edit
#Pin a message: https://docs.telethon.dev/en/latest/modules/custom.html#telethon.tl.custom.message.Message.pin        

client.start()
client.run_until_disconnected()
