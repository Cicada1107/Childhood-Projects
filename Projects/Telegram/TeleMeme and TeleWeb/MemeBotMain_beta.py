#Driver code for just the meme bot because TelegramBot 1 doesn't seem to be working

#Features to include in future:
#Get a single meme at a time and then continue getting memes one by one on command form the memes list until it is finished 

from telethon import TelegramClient, events
import re, asyncio, requests, TeleMeme

name = "Arijit Dubey"
api_id = "14630422"
api_hash = "d8d23219b71c70495455b9598d0280af"
phone = "+919433374114"
username = "Momentii1107"


client = TelegramClient("Arijit Dubey", api_id, api_hash)

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
    '''send memes to the chat using the TeleMeme module I built'''
    #the numbers specified by users start at index number 6
    #Just need to integrate my module with telegram api to set up an interaction in the chat now
    try:
        arg = event.raw_text.split()[1]
        if str(event.raw_text[6]) in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]: n,search = int(arg), None
        else: n, search = 10, arg
        memes = TeleMeme.get_memes(search = search, n = n)
        for meme in memes:
            await event.reply(meme.src + '\n' + "**__" + meme.caption + "__**", link_preview=True)
    except:
        await event.reply("**Syntax Error**\nCorrect Format: `!meme <Search (Only use one word)>OR<No. of memes>`")


client.start()
client.run_until_disconnected()