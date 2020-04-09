from telegram.ext import Updater, CommandHandler


def sms(bot, update):
    print('Send message /start')
    bot.message.reply_text('Hello i"m bot\n') # отправка ответа

def main():
    my_bot = Updater("1211557475:AAF7_m9P0rMA-i--3ltYmVSrLDnl8zaR5eI", "https://telegg.ru/orig/bot", use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))

    my_bot.start_polling()  # проверка о наличии сообщений с telegram
    my_bot.idle()  # работа пока не остановят


#if __name__ == '__main__':
main()
