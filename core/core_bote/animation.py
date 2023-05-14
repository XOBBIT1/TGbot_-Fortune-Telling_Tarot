import time

import telebot
from settings.config_settings import token

bot = telebot.TeleBot(token, parse_mode='html')


def loading(message, string, icon):
    load = string
    wait = bot.send_message(message.chat.id, load.format(f' {icon}'))
    time.sleep(1)
    bot.edit_message_text(load.format(f' {icon}{icon}️'), message.chat.id, wait.message_id)
    time.sleep(1)
    bot.edit_message_text(load.format(f' {icon}{icon}{icon}'), message.chat.id, wait.message_id)
    time.sleep(1)
    bot.edit_message_text(load.format(f' {icon}{icon}{icon}{icon}'), message.chat.id, wait.message_id)
    time.sleep(1)
    bot.edit_message_text(load.format(f' {icon}{icon}{icon}{icon}{icon}'), message.chat.id, wait.message_id)
    time.sleep(1)


def get_sticker(message):
    sticker = bot.send_sticker(message.chat.id, open("static/AnimatedSticker.tgs", "rb"))
    return sticker
