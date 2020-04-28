import telebot
import re
import sys
import config
import datetime
from parse import getDataByURL
from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.token)
now = datetime.datetime.now()

print("Connected!")


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='Ячмень', callback_data='Ячмень'),
               (telebot.types.InlineKeyboardButton(text='Пшеница', callback_data='Пшеница')))

    markup.row(telebot.types.InlineKeyboardButton(text='Семечка', callback_data=5),
               (telebot.types.InlineKeyboardButton(text='Горох', callback_data=6)))

    markup.add(telebot.types.InlineKeyboardButton(
        text='Кукуруза', callback_data=7))

    if message.chat.type == 'private':
        bot.send_message(message.chat.id, '<b>Добрый день сегодня цены на зерно следующие:</b> \n',
                         parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    start = telebot.types.ReplyKeyboardMarkup(True, True).row('/start')
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='Max и Min', callback_data=10),
               (telebot.types.InlineKeyboardButton(text='График цен', callback_data=11)))
    bot.answer_callback_query(
        callback_query_id=call.id, text='Ожидайте идёт подготовка цен!')
    if call.data == 'Ячмень':
        bot.send_message(call.message.chat.id,
                         getDataByURL(config.filter_params_dict[call.data]), parse_mode='HTML', reply_markup=start)
    elif call.data == 'Пшеница':
        bot.send_message(call.message.chat.id,
                         getDataByURL(config.filter_params_dict[call.data]), parse_mode='HTML', reply_markup=start)
    elif call.data == '5':
        bot.send_message(call.message.chat.id, 'New message')
    elif call.data == '6':
        bot.send_message(call.message.chat.id, 'New message')
    elif call.data == '7':
        bot.send_message(call.message.chat.id, 'New message')
    elif call.data == '10':
        bot.send_message(call.message.chat.id, 'New message')
    elif call.data == '11':
        bot.send_message(call.message.chat.id, 'New message')
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


try:
    bot.infinity_polling(True)
except Exception as bot_polling_error:
    print(bot_polling_error)
