#OOP Based telegram_bot_1

"""
Here I have to:
1. learn why API programs in python are structured with @client.event_reference and then async def,
2. understand how to impliment a class object system in an event based API program.
"""

#Asyncio and Event Driven Programming in python: https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_eventdriven_programming.htm
# Classes(Basic): https://www.youtube.com/watch?v=apACNr7DC_s

from telethon import TelegramClient, events
from configparser import ConfigParser
from bs4 import BeautifulSoup as bs
import re, asyncio, requests, music
from urllib.parse import urlparse
import spotify_sync as spotify

#using condfig parser to migtrate telegram info
config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("Arijit Dubey", api_id, api_hash)


memes = []


#class Command:
    '''A command for the telegram_bot to exeute'''
#    def __init__(self, help_text, pattern):



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
        dad = re.match(r".*(I'm|I am|My name is|i'm|i am|my name is|me am|Me is)\s+.*", event.raw_text, re.IGNORECASE)
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
    '''This function detects links with https protocol in the msgs and finds the host/website name'''
    match = re.search(r".*(https://|http://).+", msg.raw_text)
    if match:
        url = match.group()
        website = urlparse(url).hostname
        print('Url detected:', url)
        await msg.reply("Link detected: {}\nWebsite: {}".format(url, website), link_preview=False)


@client.on(events.NewMessage(pattern = r"(?i)^!meme"))
async def meme(event):
    if len(memes) == 0:
        url = 'https://www.memedroid.com/memes/latest'  #'https://www.memedroid.com/memes/top/day'
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        #img_tag = soup.find('img','img-responsive grey-background')
        #meme_link = img_tag['src']
        imgs = soup.select('img[src^="https://images3.memedroid.com/images"]')
        for img in imgs:
            memes.append(img['src'])
    for i in memes:
        await event.reply(i)
        memes.remove(i)
        break


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

@client.on(events.NewMessage(pattern = r"(?i)^!music"))
async def music():
    


client.start()
client.run_until_disconnected()
