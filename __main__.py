import telebot
import re
import sys
import config
import datetime
from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.token)
now = datetime.datetime.now()

print("Connected!")


@bot.message_handler(commands=['start'])
def start_message(message):

    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='Ячмень', callback_data=3),
               (telebot.types.InlineKeyboardButton(text='Пшеница', callback_data=4)))

    markup.row(telebot.types.InlineKeyboardButton(text='Семечка', callback_data=5),
               (telebot.types.InlineKeyboardButton(text='Горох', callback_data=6)))

    markup.add(telebot.types.InlineKeyboardButton(
        text='Кукуруза', callback_data=7))

    if message.chat.type != 'private':
        bot.send_message(message.chat.id, '<b>Добрый день сегодня цены на зерно следующие:</b> \n',
                         parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(
        callback_query_id=call.id, text='Ожидайте идёт подготовка цен!')
    answer = ''
    if call.data == '3':
        answer = 'Цена на Пшеницу {}'.format(now.strftime('%d %B'))
    elif call.data == '4':
        answer = 'Цена на Семечка {}'.format(
            "без НДС 15.45 руб/кг, с НДС +10%")
    elif call.data == '5':
        answer = 'Цена на Горох'
    elif call.data == '6':
        answer = 'Цена на ячмен'
    elif call.data == '7':
        answer = 'Цена на Кукурузу'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


try:
    bot.infinity_polling(True)
except Exception as bot_polling_error:
    print(bot_polling_error)
