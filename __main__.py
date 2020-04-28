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

web = 'https://rif-rostov.ru/price/?arCrops%5B%5D=127'


@bot.message_handler(commands=['start'])
def start_message(message):

    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='Ячмень', callback_data='Ячмень'),
               (telebot.types.InlineKeyboardButton(text='Пшеница', callback_data='Пшеница')))

    markup.row(telebot.types.InlineKeyboardButton(text='Семечка', callback_data='Семечка'),
               (telebot.types.InlineKeyboardButton(text='Горох', callback_data='Горох')))

    markup.add(telebot.types.InlineKeyboardButton(
        text='Кукуруза', callback_data='Кукуруза'))

    if message.chat.type == 'private':
        bot.send_message(message.chat.id, '<b>Добрый день сегодня цены на зерно следующие:</b> \n',
                         parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    start_button = telebot.types.ReplyKeyboardMarkup(True, True).row('/start')

    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='Max и Min', callback_data=10),
               (telebot.types.InlineKeyboardButton(text='График цен', callback_data=11)))

    bot.answer_callback_query(
        callback_query_id=call.id, text='Ожидайте идёт подготовка цен!')
    if call.data == 'Ячмень':
        bot.send_message(call.message.chat.id, 'New message',
                         reply_markup=start_button)
    elif call.data == 'Пшеница':
        bot.send_message(call.message.chat.id,
                         getDataByURL(web), parse_mode='HTML', reply_markup=start_button)
    elif call.data == 'Семечка':
        bot.send_message(call.message.chat.id, 'New message',
                         reply_markup=start_button)
    elif call.data == 'Горох':
        bot.send_message(call.message.chat.id, 'New message',
                         reply_markup=start_button)
    elif call.data == 'Кукуруза':
        bot.send_message(call.message.chat.id, 'New message',
                         reply_markup=start_button)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


try:
    bot.infinity_polling(True)
except Exception as bot_polling_error:
    print(bot_polling_error)
