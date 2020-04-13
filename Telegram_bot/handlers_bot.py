from bs4 import BeautifulSoup
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler

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


def form_start(bot, update):
    bot.message.reply_text('What is you name? ', reply_markup=ReplyKeyboardRemove)
    return 'user_name'


def form_comment(bot, update):
    update.user_data['comment'] = bot.message.text
    text = """Results:
    <b>Name: </b> {name}
    <b>Age: </b> {age}
    <b>Rating: </b> {evaluation}
    <b>Comment: </b> {comment}
    """.format(**update.user_data)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text('Thanks for you comment', reply_marckup=get_keyboard())
    return ConversationHandler.END


def form_exit_comment(bot, update):
    text = """Results:
    <b>Name: </b> {name}
    <b>Age: </b> {age}
    <b>Rating: </b> {evaluation}""".format(**update.user_data)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text("Thanks", reply_markup=get_keyboard())
    return ConversationHandler.END


def dontKnow(bot, update):
    bot.message.reply_text('I"m not understand')
