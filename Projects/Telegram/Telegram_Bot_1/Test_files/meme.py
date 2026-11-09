#Meme_getter
#Use try except for finding the src(so that it only gives images for now)
#The same problem as mine:
#https://stackoverflow.com/questions/66494972/beautiful-soup-find-all-not-returning-all-elements
#Add the n number of memes thing to the command so as to make it work better
#Use tqdm to implement a loading bar
#make another function for refreshing the memes list with new memes once it's empty(or make it dependent on time?)
#as of now the loader camn only get upto 17 memes. Reason: possibly because the websites loads only a specific number of memes and then loads more as we scroll.

from bs4 import BeautifulSoup as bs
from telethon import TelegramClient, events
import re, asyncio, requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']

client = TelegramClient("Arijit Dubey", api_id, api_hash)

def get_memes():
    #so for now this gives like 17 memes. For more I have to probably use json etc because the rest of the memes are loaded as we scroll
    memes = []
    url = 'https://www.memedroid.com/memes/latest'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    #img_tag = soup.select('img[src^="https://images3.memedroid.com/images"]')
    imgs = soup.find_all(class_ = "img-responsive grey-background")
    [memes.append(i['src']) for i in imgs]
    return memes

def refresh_memes(l: list):
    #takes in the original list acquired from the get_memes() function and then refreshes it
    #This is supposed to refresh it with new unique memes that haven't been already acquired
    pass

memes = []

@client.on(events.NewMessage(pattern = r"(?i)^!meme"))
async def meme(event):
    #the try except block etc is just temporary way to send all memes. Optimise it later on.
    n = event.raw_text.split()[1]
    global memes
    if len(memes) == 0:
        memes += get_memes()
    all = re.match('.*all.*', n, re.IGNORECASE)
    if all:
        n = len(memes)
    else:
        try:
            n = int(n)
        except (IndexError, ValueError):
            n = 1
    for i in range(n):
        await event.reply(memes.pop())


client.start()
client.run_until_disconnected()
            
