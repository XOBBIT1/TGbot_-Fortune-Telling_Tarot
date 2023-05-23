import time

import telebot
from settings.config_settings import token

bot = telebot.TeleBot(token, parse_mode='html')


def loading(message, string, icon):
    load = string
    wait = bot.send_message(message.chat.id, load.format(f' {icon}'))
    for i in range(2, 7):
        time.sleep(1)
        bot.edit_message_text(load.format(f' {icon * i}'), message.chat.id, wait.message_id)


def get_sticker(message):
    sticker = bot.send_sticker(message.chat.id, open("static/AnimatedSticker.tgs", "rb"))
    return sticker
