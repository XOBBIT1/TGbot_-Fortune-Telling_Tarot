import telebot

from core.core_bote.animation import bot
from core.repository.queries import add_user


@bot.message_handler(content_types=["text"])
def button_take_card(message):
    add_user(message)
    bot.send_sticker(message.chat.id, open("static/AnimatedSticker.tgs", "rb"))
    if message.chat.type == "private":
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        button1 = telebot.types.InlineKeyboardButton("Узнать свою карту 🔮", callback_data="fortune")

        markup.add(button1)

        bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b>\n"
                                          f"Хочешь узнать, что тебя ждёт сегодня?😏\n"
                                          f"Кликай и всё <b>станет понятно</b> ..........👇\n", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Ваша судьба не понятна!")


@bot.message_handler(content_types=["text"])
def keyboard(message):
    if message.chat.type == "private":
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        button1 = telebot.types.InlineKeyboardButton("Любовь", callback_data="love")
        button2 = telebot.types.InlineKeyboardButton("Работа", callback_data="work")
        button3 = telebot.types.InlineKeyboardButton("На ситуацию", callback_data="issue")
        button4 = telebot.types.InlineKeyboardButton("Финансы", callback_data="money")
        button5 = telebot.types.InlineKeyboardButton("Здоровье", callback_data="health")
        button6 = telebot.types.InlineKeyboardButton("Духовное значение", callback_data="spirit")

        markup.add(button1, button2, button3, button4, button5, button6)

        bot.send_message(message.chat.id, f"У данной карты есть ещё пару значений.\n"
                                          f"Для простоты мы разбили их на <b>Темы</b>\n"
                                          f"Кликай на то, что тебя больше интересует. \n"
                                          f"Возможно именно это и поможет тебе в принятии решений )\n", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Ваша судьба не понятна!")
