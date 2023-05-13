from core.core_bote.callbacks import callback_fortune_button
from core.core_bote.animation import bot
from core.core_bote.keyboards import button_take_card


@bot.message_handler(commands=["start"])
def start(message):
    button_take_card(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    callback_fortune_button(call)


print("Bot nachal rabotu !")

bot.polling(none_stop=True)
