import telebot

from core.core_bote.animation import bot, get_sticker
from core.services.queries import add_user


def button_take_card(message):
    add_user(message)
    get_sticker(message)
    if message.chat.type == "private":
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        button1 = telebot.types.InlineKeyboardButton("Узнать свою карту на сегодня 🔮", callback_data="fortune")
        button2 = telebot.types.InlineKeyboardButton("Расклад всё тебе расскжет", callback_data="layout")

        markup.add(button1, button2)

        bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b> 👋\n"
                                          f"Хочешь узнать, <b>свою карту</b> на сегодня?😏\n"
                                          f"Кликай и всё <b>станет понятно</b> ..........👇\n"
                                          f"\n"
                                          f"Если же тебе захочется выбрать новую карту, то просто напиши мне)😁\n"
                                          f"\n"
                                          f"\n"
                                          f"<b>P.S : Пиши всё что захочешь я всё пойму)</b>",  reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Ваша судьба не понятна!")


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
                                          f"Для простоты мы разбили их на <b>Темы</b> 📋\n"
                                          f"Кликай 👇 на то, что тебя больше интересует. \n"
                                          f"Возможно именно это и поможет тебе в принятии решений 😏)\n", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Ваша судьба не понятна!")


def button_take_new_card(message):
    get_sticker(message)
    if message.chat.type == "private":
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        button1 = telebot.types.InlineKeyboardButton("Узнать новую карту🔮", callback_data="new_card")
        button2 = telebot.types.InlineKeyboardButton("Расклад всё тебе расскжет", callback_data="layout")

        markup.add(button1, button2)

        bot.send_message(message.chat.id, f"<b>Хочешь узанть новую карту?</b>\n"
                                          f"<i>Хм.................</i>\n"
                                          f"Кликай на кнопку👇 и узнай свою судьбу\n", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Ваша судьба не понятна!")
