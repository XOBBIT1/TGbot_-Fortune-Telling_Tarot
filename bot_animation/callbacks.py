import random
import time

from core.get_data_from_db import get_data_by_name
from bot_animation.animation import bot, loading
from bot_animation.keyboards import keyboard
from my_settings.bd.models import Cards
from my_settings.config_settings import common_phrases, emojis


def callback_fortune_button(call):
    try:
        if call.message:
            if call.data == "fortune":
                for card_data in get_data_by_name(Cards):
                    loading(call.message, 'Тасуем карты {}', "🀧")
                    bot.send_message(call.message.chat.id, f"Ваш <b>АРКАН</b>: {card_data.harness}")
                    time.sleep(2)
                    bot.send_message(call.message.chat.id, f"Ваша <b>КАРТА</b> это - <b>{card_data.card_name}</b>")
                    time.sleep(2)
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_message(call.message.chat.id, f"Значение <b>Карты</b>: \n"
                                                           f"<i> {card_data.card_description}</i>")
                    time.sleep(1)
        callback_topics(call)
        time.sleep(3)
        keyboard(call.message)
    except Exception as e:
        print(repr(e))


def callback_topics(call):
    try:
        if call.message:
            if call.data == "love":
                loading(call.message, random.choice(common_phrases), random.choice(emojis))
                bot.send_message(call.message.chat.id, f"В разарботке")
            elif call.data == "work":
                loading(call.message, random.choice(common_phrases), random.choice(emojis))
                bot.send_message(call.message.chat.id, f"В разарботке")
            elif call.data == "issue":
                loading(call.message, random.choice(common_phrases), random.choice(emojis))
                bot.send_message(call.message.chat.id, f"В разарботке")
            elif call.data == "money":
                loading(call.message, random.choice(common_phrases), random.choice(emojis))
                bot.send_message(call.message.chat.id, f"В разарботке")
            elif call.data == "health":
                loading(call.message, random.choice(common_phrases), random.choice(emojis))
                bot.send_message(call.message.chat.id, f"В разарботке")
            elif call.data == "Spirit":
                loading(call.message, random.choice(common_phrases), random.choice(emojis))
                bot.send_message(call.message.chat.id, f"В разарботке")

    except Exception as e:
        print(repr(e))
