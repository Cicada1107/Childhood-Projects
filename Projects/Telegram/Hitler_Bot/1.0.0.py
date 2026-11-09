#Telegram bot "Hitler" 1.0.0

from telegram import *
from telegram.ext import *
import logging


bot = Bot("1688932304:AAESFCA_cFbmxa2KLyw68EcIUf9yBFJuH8I")

updater = Updater("1688932304:AAESFCA_cFbmxa2KLyw68EcIUf9yBFJuH8I", use_context=True)

dispatcher = updater.dispatcher

#Command 1:-
def test_function(update=Update, context=CallbackContext):
    bot.send_message(chat_id = update.effective_chat.id, text = "Test run.")

start_value = CommandHandler('Test', test_function)

#Command 2:-
#def spam(update=Update, context=CallbackContext):
    #spam command here

dispatcher.add_handler(start_value)

updater.start_polling()

#OH COME ON!!!!!!!!
