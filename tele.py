import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import logging


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
log = logging.getLogger("telebot")


TOKEN = ""


def start(update, context):
    update.message.reply_text("""
    Welcome, teleBot started!

    Here are the functions below:

    /start -> Welcome Message
    /help -> This Message
    /content ->  bot status write anything here
    
    """)


def help(update, context):
    update.message.reply_text("""
    
    /start -> Welcome Message
    /help -> This Message
    /content -> bot status write anything here
    
    """)


def content(update, context):
    update.message.reply_text("Welcome to tele bot :) what the bot should do:")



def main():

    updater = telegram.ext.Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler(
        "start", start, Filters.user(username="@username"))) #put your own username here

    dispatcher.add_handler(CommandHandler(
        "help", help, Filters.user(username="@username")))

    dispatcher.add_handler(CommandHandler(
        "content", content, Filters.user(username="@username")))

  
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
