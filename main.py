from bot_animation.callbacks import callback_fortune_button, callback_topics
from bot_animation.animation import bot
from bot_animation.keyboards import button_take_card, keyboard


@bot.message_handler(commands=["start"])
def start(message):
    button_take_card(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    callback_fortune_button(call)


print("Bot nachal rabotu !")

bot.polling(none_stop=True)
