import random
import time

from core.services.queries import get_data_by_name
from core.core_bote.animation import bot, loading
from core.core_bote.keyboards import keyboard
from settings.bd.models import Cards
from settings.config_settings import common_phrases, emojis


def callback_fortune_button(call):
    try:
        global data_form_base
        if call.message:
            if call.data == "fortune" or "new_card":
                data_form_base = get_data_by_name(Cards)
                for card_data in data_form_base:
                    loading(call.message, 'Тасуем карты {}', "🀧")
                    bot.send_message(call.message.chat.id, f"Ваш <b>АРКАН</b>: {card_data.harness}")
                    time.sleep(2)
                    bot.send_message(call.message.chat.id, f"Ваша <b>КАРТА</b> это - <b>{card_data.card_name}</b>")
                    time.sleep(2)
                    bot.send_photo(call.message.chat.id, f"{card_data.images.img_url}")
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_message(call.message.chat.id, f"Значение <b>Карты {card_data.card_name}</b>: \n"
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
            for card_data in data_form_base:
                if call.data == "love":
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_sticker(call.message.chat.id, open("static/AnimatedStickerLove.tgs", "rb"))
                    bot.send_message(call.message.chat.id, f"Значение <b>Карты {card_data.card_name}</b>"
                                                           f" в <b>Любви</b>: \n "
                                                           f"<i>{card_data.descriptions.love_description}</i>")
                elif call.data == "work":
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_sticker(call.message.chat.id, open("static/AnimatedStickerWork.tgs", "rb"))
                    bot.send_message(call.message.chat.id, f"Значение <b>Карты {card_data.card_name}</b>"
                                                           f" в <b>Работе</b>: \n"
                                                           f"<i>{card_data.descriptions.work_description}</i>")
                elif call.data == "issue":
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_sticker(call.message.chat.id, open("static/AnimatedStickerIssue.tgs", "rb"))
                    bot.send_message(call.message.chat.id, f"Значение <b>Карты {card_data.card_name}</b>"
                                                           f"на <b>Ситуацию</b>: \n"
                                                           f"<i>{card_data.descriptions.issue_description}</i>")
                elif call.data == "money":
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_sticker(call.message.chat.id, open("static/AnimatedStickerMoney.tgs", "rb"))
                    bot.send_message(call.message.chat.id, f"Значение <b>Карты {card_data.card_name}</b>"
                                                           f" в <b>Финансах</b>: \n"
                                                           f"<i>{card_data.descriptions.money_description}</i>")
                elif call.data == "health":
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_sticker(call.message.chat.id, open("static/AnimatedStickerHealth.tgs", "rb"))
                    bot.send_message(call.message.chat.id, f"Значение <b>Карты {card_data.card_name}</b>"
                                                           f" в <b>Здоровье</b>: \n"
                                                           f"<i>{card_data.descriptions.health_description}</i>")
                elif call.data == "spirit":
                    loading(call.message, random.choice(common_phrases), random.choice(emojis))
                    bot.send_sticker(call.message.chat.id, open("static/AnimatedStickerSpirit.tgs", "rb"))
                    bot.send_message(call.message.chat.id, f"Духовное значение <b>Карты</b>: \n"
                                                           f"<i>{card_data.descriptions.spirit_description}</i>")

    except Exception as e:
        print(repr(e))
        bot.send_message(call.message.chat.id, f"Бот недавно перезагружался, "
                                               f"поэтому у вас пока нет карты.😢\n"
                                               f"<b>Напиши мне и выбирай новую карту !</b>\n"
                                               f"Или кликай на 👉 /start ")


