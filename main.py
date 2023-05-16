import time
import logging

from settings import config_settings, logging_settings
from core.core_bote.callbacks import callback_fortune_button, callback_topics
from core.core_bote.animation import bot
from core.core_bote.keyboards import button_take_card, keyboard, button_take_new_card

logging_settings.setup_logger()

logging.info("Bot nachal rabotu !")


@bot.message_handler(commands=["start"], content_types=["text"], func=lambda call: True)
def start(message):
    config_settings.IS_POSITING_REQUESTED = True
    button_take_card(message)


@bot.message_handler(content_types=["text"],  func=lambda call: True)
def new_card(message):
    config_settings.IS_POSITING_REQUESTED = True
    button_take_new_card(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if config_settings.IS_POSITING_REQUESTED:
        callback_fortune_button(call)
        config_settings.IS_POSITING_REQUESTED = False
    else:
        callback_topics(call)
        time.sleep(2)
        keyboard(call.message)


bot.polling(none_stop=True)
