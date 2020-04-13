# function create keyboard
# function about create form

from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def get_keyboard():
    contact_button = KeyboardButton('Send Contacts', request_contact=True)
    location_button = KeyboardButton('Send GeoPosition', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([['Start', 'Joke'],
                                       [contact_button, location_button]],
                                      ['fill out in form'],
                                      resize_keyboard=True)
    return my_keyboard


def form_start(bot, update):
    bot.message.reply_text('What is you name? ', reply_markup=ReplyKeyboardRemove)
    return 'user_name'


def form_get_name(bot, update):
    update.user_data['name'] = bot.message.text
    bot.message.reply_text('How old you? ')
    return 'user_age'


def form_get_age(bot, update):
    update.user_data['age'] = bot.message.text
    reply_keyboard = [["1", "2", "3", "4", "5"]]
    bot.message.reply_text('Rate this form (1-5): ',
                           reply_markup=ReplyKeyboardMarkup(
                               reply_keyboard,
                               resize_keyboard=True,
                               one_time_keyboard=True))
    return 'evaluation'


def form_get_evaluation(bot, update):
    update.user_data['evaluation'] = bot.message.text
    reply_keyboard = [['Less_Keyboard']]  # create keyboard
    bot.message.reply_text('Write your review or skip',
                           reply_markup=ReplyKeyboardMarkup(
                               reply_keyboard,
                               resize_keyboard=True,
                               one_time_keyboard=True))
    return 'comment'
