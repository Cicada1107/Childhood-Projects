#The seoond learning file for the telethon library
#https://docs.telethon.dev/en/latest/basic/quick-start.html

#entities:
#https://docs.telethon.dev/en/latest/concepts/entities.html

from telethon import TelegramClient, events
import re
import time

name = "Arijit Dubey"
api_id = "14630422"
api_hash = "d8d23219b71c70495455b9598d0280af"
phone = "+919433374114"
username = "Momentii1107"

client = TelegramClient("Arijit Dubey", api_id, api_hash)


'''
@client.on(events.NewMessage)
async def replier(event):
    #phrase = re.match(r"^*")
    user = await event.get_sender()
    #print(user.username)
    if user.username == "gamerXgo_1974":
        print("Sender recognised: {}\n message content: {}\nResponse_sent: 'Oh ok np'".format(user.username, event.raw_text))
        if "sorry" in event.raw_text:
            await event.reply("Oh ok np")
        elif "Sorry" in event.raw_text:
            await event.reply("Oh ok np")

@client.on(events.NewMessage)
async def responder(event):
    user = await event.get_sender()
    if user.username == "gamerXgo_1974":
        print("Sender recognised: {}\n message content: {}\nResponse_sent: 'Uhmmm...'".format(user.username, event.raw_text))
        await event.reply("Uhmmm...")
    else:
        print("Sender id not recognized")
        print("Sender username: {}".format(user.username))

@client.on(events.NewMessage)
async def dad(event):
    user = await event.get_sender()
    if user.username != "Momentii1107":
        txt = str(event.raw_text)
        phrase = re.match(r"(^I'm|I am|My name is|i'm|i am|my name is)\s+(.*)", txt, re.IGNORECASE)
        if phrase != None:
            await event.reply("Hi " + phrase.group(2) + ' ' + phrase.group(1) + " dad")

#@client.on(events.NewMessage)
#async def replier(event):
    #print(event.sender_id)


slangs = ["heck", "hell", 'fuck', 'Fuck', 'sex']

@client.on(events.NewMessage)
async def filter(event):
    for i in event.raw_text:
        if i in slangs:
            await event.delete()

class main():
    async def Me():
        me = await client.get_me()
        print(me.stringify())
        print(me.username)
        print(me.phone)

    async def ping():
        await client.send_message("+91 99032 92350", "`User_not_found_error: User status_check timed out`")

    async def check_status(user):
        pass

#with client:
#    client.loop.run_until_complete(main.ping())
'''

client.start()
client.run_until_disconnected()
