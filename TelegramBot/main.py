import telebot
from telebot import types
from random import randrange

token = #token
bot = telebot.TeleBot(token)

jokes = [ 'Идут по лесу дюймовочка, белоснежка и армяне. Дюймовочка говорит: "Я самая маленькая на Земле", Белоснежка: "Я самая красивая на земле", армяне: "Мы больше всех играем в нарды". Идут они, в общем, и заходят в Дом Правды. Дюймовочка выбегает со слезами и говорит, что она не самая маленькая. Белоснежка тоже выходит и плачет, говорит, что она не самая kрасивая. Армяне выходят капец довольными', 'Почему слепой мальчик уронил шоколадное мороженное? Его сбила фура', 'Муж на смертном одре. Лежит, умирает и зовет жену.\n-Дорогая, скажи, почему наш шестой ребенок не похож на остальных? У него другой отец?\nЖена вся в слезах\n-Да, у него другой отец\n-Кто?\n-Ты ', 'Играют 2 мужика с Альцгеймером:\n- Это ты походил конем?\n-Ты кто?', 'Когда идет дождь, моя девушка смотрит в окно. Но иногда я впускаю её домой' ]


@bot.message_handler(commands = ['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Hello!\ntype /help to see the list of commands', reply_markup = keyboard)


@bot.message_handler(commands = ['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'I can:\n/mtuci -show you fresh information about MTUCI\n/joke -tell you a joke\n/weather -show you the current weather in Moscow\n')
    bot.send_message(message.chat.id, 'I also can communicate with you. Try typing:\n-Hello\n-Goodbye\n-Mtuci')

@bot.message_handler(commands = ['mtuci'])
def info(message):
    bot.send_message(message.chat.id, 'Here you go: http://mtuci.ru')


@bot.message_handler(commands = ['joke'])
def joke(message):
    bot.send_message(message.chat.id, str(jokes[ randrange(5) ]))

@bot.message_handler(commands = ['weather'])
def weather(message):
    bot.send_message(message.chat.id, "Here you go: http://yandex.ru/pogoda/maps/nowcast")


@bot.message_handler(content_types = ['text'])
def answer(message):
    if message.text.lower() == "mtuci":
        bot.send_message(message.chat.id, 'Here you go - https://mtuci.ru/')
    elif message.text.lower() == "hello":
        bot.send_message(message.chat.id, 'Hi!')
    elif message.text.lower() == "goodbye":
        bot.send_message(message.chat.id, 'Have a nice day!')

bot.infinity_polling()
