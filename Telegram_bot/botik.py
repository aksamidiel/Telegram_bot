from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from .settings import TG_TOKEN, TG_API_URL
from .handlers_bot import *
from .util import *


def get_keyboard():  # создание клавиатуры и ее разметки
    my_key = ReplyKeyboardMarkup([['Joke'], ['Start']], resize_keyboard=True)
    return my_key


def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))  # обработчик комманды start

    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Joke'), get_jokes))  # обработчик текстового сообщения
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, par))  # обработчик текстового сообщения
    my_bot.start_polling()  # проверка о наличии сообщений с telegram
    my_bot.dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))  # обработчик полученого контакта
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, get_location))
    my_bot.idle()  # работа пока не остановят


if __name__ == '__main__':
    main()
