# function create keyboard

from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard():
    contact_button = KeyboardButton('Send Contacts', request_contact=True)
    location_button = KeyboardButton('Send GeoPosition', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([['Start', 'Joke'],
                                       [contact_button, location_button]], resize_keyboard=True)
    return my_keyboard
