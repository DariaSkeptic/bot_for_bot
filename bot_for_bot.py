from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я бот для приёма заказов.')

def main():
    # Получаем токен из .env
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
