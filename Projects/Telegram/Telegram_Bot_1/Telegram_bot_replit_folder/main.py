from telethon import TelegramClient, events, types
import re, csv, asyncio, os, requests
from datetime import date, datetime
from keep_alive import keep_alive
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
import RickrollDetector as rdr

name = os.getenv('name')
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
phone = os.getenv('phone')
username = os.getenv('username')

client = TelegramClient(name, api_id, api_hash)


def get_memes():
    memes = []
    url = 'https://www.memedroid.com/memes/latest'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    #img_tag = soup.select('img[src^="https://images3.memedroid.com/images"]')
    imgs = soup.find_all(class_ = "img-responsive grey-background")
    [memes.append(i['src']) for i in imgs]
    return memes


memes = []

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
    user = await event.get_sender()
    if user.username == "gamerXgo_1974":
        ditch = re.match(r".*(sorry)\s*", event.raw_text, re.IGNORECASE)
        dad = re.match(r"^(I prolly am|I probably am|I'm|I am|My name is|i'm|i am|my name is|me is|me am)\s+.*", event.raw_text, re.IGNORECASE)
        if ditch:
            if not dad:
                await event.reply("Oh ok np")

@client.on(events.NewMessage)
async def replier(event):
    user = await event.get_sender()
    if user.username == "gamerXgo_1974":
        ttyl = re.match(r".*(ttyl)\s*", event.raw_text, re.IGNORECASE)
        if ttyl:
          await event.reply("fair enough")
      

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


@client.on(events.NewMessage)
async def dad(event):
    user = await event.get_sender()
    if user.username != "Momentii1107":
        phrase = re.match(r".*(I'm|I am|My name is|i'm|i am|my name is|me is)\s+(.*)", event.raw_text, re.IGNORECASE)
        if phrase:
            await event.reply("Hi " + phrase.group(2) + ' ' + phrase.group(1) + " Arijit")


@client.on(events.NewMessage(pattern = r"(?i).*(fuck|hell|ass|sex|fook|faggot|chutiya|bsd|bhosri|bhosdi|wtf|tf).*"))
async def mod(event):
    await asyncio.sleep(25)
    await event.delete()

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

@client.on(events.NewMessage(pattern = r"(?i)^!meme"))
async def meme(event):
    #the try except block etc is just temporary way to send all memes. Optimise it later on.
    #n = event.raw_text.split()[1]
    global memes
    if len(memes) == 0:
        memes += get_memes()
    await event.reply(memes.pop())

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
            
keep_alive()
client.start()
client.run_until_disconnected()
