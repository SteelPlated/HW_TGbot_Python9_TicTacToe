from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler
from Cross import*

bot = Bot(token='5572182114:AAEGaREq4XiSrXJdUjxRNteu2Bd0pBD4VUM')
updater = Updater(token='5572182114:AAEGaREq4XiSrXJdUjxRNteu2Bd0pBD4VUM')
updater.dispatcher.add_handler(CommandHandler('Cross', cross))





# В конце |||
updater.start_polling()
updater.idle()