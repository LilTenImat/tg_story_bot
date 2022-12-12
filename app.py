import telebot
import sys

def main(args):
    TOKEN = ''
    TEXT = ''
    text = 'text.txt'
    token = 'token.txt'

    if len(args) < 2:
        print('No args given. Using default "token.txt" and "text.txt". ')
    elif len(args) == 2:
        print(f'One argument given. Using {args[1]} as token file name.')
        token = args[1]
    elif len(args) == 3:
        print(f'Using {args[1]} as token file name.\nUsing {args[2]} as token file name.')
        token, text = args[1], args[2]
    else:
        print('Too many args given. Exiting...')
        return

    
    with open(text, encoding='utf-8') as file:
        TEXT = file.read()
    with open(token, encoding='utf-8') as file:
        TOKEN = file.read()


    if len(TEXT.strip()) == 0:
        TEXT = 'Invalid text'

    bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
    @bot.message_handler(commands=['start'])
    def send_story(message):
        bot.send_message(message.chat.id, TEXT, "HTML")
    
    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.send_message(message.chat.id, "This bot can only give you it's text after /start command")

    print('Your bot is running...\nCtrl+C to stop')
    bot.infinity_polling()


if __name__ == '__main__':
    main(sys.argv)