#sos

from telethon import TelegramClient, events
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
name = config['Telegram']['name']
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']

client = TelegramClient("Arijit Dubey", api_id, api_hash)


@client.on(events.NewMessage(pattern = r"(?i)^!sos"))
async def sos(event):
    """Deletes all own messages in a chat in case of emergency"""
    await event.delete()
    chat = event.chat_id
    msgs = await client.get_messages(chat, 700)
    for msg in msgs:
        user = await msg.get_sender()
        if user.username == "Momentii1107": await msg.delete()
    print("Procedure completed succesfully")

client.start()
client.run_until_disconnected()
