from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from Telegram_bot.settings import TG_TOKEN, TG_API_URL
from bs4 import BeautifulSoup
import requests


def sms(bot, update):
    print('Send message /start')
    my_keyboard = ReplyKeyboardMarkup([['/start', 'start'], ['Начать']])   #добавление кнопочки
    bot.message.reply_text('Hello i"m bot {}\n'.format(bot.message.chat.first_name),
                           reply_markup=my_keyboard)  # отправка ответа
    print(bot.message())  # печать сообщения в консоль

def get_jokes(bot, update):
    receive = requests.get('http://anekdotme.ru/random') #запрос на страницу сайта
    page = BeautifulSoup(receive.text, 'html.parser')
    find = page.select('.anekdot_text')
    for text in find:
        page = (text.getText().strip())
    bot.message.reply_text(page)


def par(bot, update):  # ресивер отправленного сообщения
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))  # обработчик комманды start

    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Joke'), get_jokes))  # обработчик текстового сообщения
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, par))  # обработчик текстового сообщения
    my_bot.start_polling()  # проверка о наличии сообщений с telegram
    my_bot.idle()  # работа пока не остановят


if __name__ == '__main__':
    main()
