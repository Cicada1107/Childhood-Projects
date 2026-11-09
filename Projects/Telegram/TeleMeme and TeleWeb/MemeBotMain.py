#Driver code for just the meme bot because TelegramBot 1 doesn't seem to be working

#Features to include in future:
#Get a single meme at a time and then continue getting memes one by one on command form the memes list until it is finished
#Current method: Get 100 memes when the bot comes online and store it in the memes list then just push one out every time a user calls for
#a meme
#future featrures: Support for videos etc and like counter

from telethon import TelegramClient, events
import re, asyncio, requests, TeleMeme

name = "Arijit Dubey"
api_id = "14630422"
api_hash = "d8d23219b71c70495455b9598d0280af"
phone = "+919433374114"
username = "Momentii1107"


client = TelegramClient("Arijit Dubey", api_id, api_hash)
memes = []

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
    '''Adds meme type objects to the memes list if it is empty and then pushes out and sends the first meme from the memes list to the chat
    or searches for a query and sends results in chat'''
    #the numbers specified by users start at index number 6
    if len(event.raw_text) == 5:#If search = false
        global memes
        if memes == []:
            print("Loading memes")
            await event.reply("`Loading memes\nEstimated time: 11 seconds`")
            memes = TeleMeme.get_memes(n = 100)
            print("Memes loaded")
            await event.reply("``Memes loaded succesfully``")
        await event.reply("{}\n**__{}__**".format(memes[0].src, memes[0].caption))#Returning first meme from the memes lists
        print("Meme sent")
        memes.pop(0)#pushing out the sent meme from the memes list
    else:#if there is a search query in the command sent by user, display 10 search results instead
        search = event.raw_text.split()[1]
        search_results = TeleMeme.get_memes(search = search)
        try:
            [await event.reply("{link}\n**__{caption}__**".format(link = i.src, caption = i.caption)) for i in search_results]
        except TypeError:
            await event.reply("`No Memes found for the given search query`")
    

client.start()
client.run_until_disconnected() 