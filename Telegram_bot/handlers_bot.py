from bs4 import BeautifulSoup
from util import get_keyboard
import requests


def sms(bot, update):
    print('Send message /start')
    bot.message.reply_text('Hello i"m bot {}\n'.format(bot.message.chat.first_name),
                           reply_markup=get_keyboard())  # отправка ответа
    print(bot.message())  # печать сообщения в консоль

# function recieve contact
def get_contact(bot, update):
    print(bot.message.contact)
    bot.message.reply_text('{}, we recieve your telephone number'.format(bot.message.chat.first_name))

# function recive location
def get_location(bot, update):
    print(bot.message.location)
    bot.message.reply_text('{}, we recieve your location'.format(bot.message.chat.first_name))


def get_jokes(bot, update):
    receive = requests.get('http://anekdotme.ru/random')  # запрос на страницу сайта
    page = BeautifulSoup(receive.text, 'html.parser')
    find = page.select('.anekdot_text')
    for text in find:
        page = (text.getText().strip())
    bot.message.reply_text(page)


def par(bot, update):  # ресивер отправленного сообщения
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)