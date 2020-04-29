import telebot
import re
import sys
import config
import datetime
import parse
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

    markup.row(telebot.types.InlineKeyboardButton(text='Семечка', callback_data='Семечка'),
               (telebot.types.InlineKeyboardButton(text='Горох', callback_data='Горох')))

    markup.add(telebot.types.InlineKeyboardButton(
        text='Кукуруза', callback_data='Кукуруза'))

    if message.chat.type == 'private':
        bot.send_message(message.chat.id, '<b>Добрый день сегодня цены на зерно следующие:</b> \n',
                         parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    start = telebot.types.ReplyKeyboardMarkup(True, True).row('/start')

    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='max и min цена', callback_data='max_min'),
               (telebot.types.InlineKeyboardButton(text='График цен', callback_data='price_graph')))

    bot.answer_callback_query(
        callback_query_id=call.id, text='Ожидайте идёт подготовка цен!')
    if call.data == 'Ячмень':
        markup.row(telebot.types.InlineKeyboardButton(text='max и min цена', callback_data= call_data + 'max')
        bot.send_message(call.message.chat.id,
                         parse.dataToString(parse.getDataByURL(
                             config.filter_params_dict[call.data]), call.data), parse_mode='HTML', reply_markup=markup)
    elif call.data == 'Пшеница':
        bot.send_message(call.message.chat.id,
                         parse.dataToString(parse.getDataByURL(
                             config.filter_params_dict[call.data]), call.data), parse_mode='HTML', reply_markup=markup)
    elif call.data == 'Семечка':
        bot.send_message(call.message.chat.id, 'Отсутствует')
    elif call.data == 'Горох':
        bot.send_message(call.message.chat.id, 'Отсутствует')
    elif call.data == 'Кукуруза':
        bot.send_message(call.message.chat.id, 'Отсутствует')
    elif call.data == 'max_min':
        bot.send_message(call.message.chat.id,
                         parse.getMaxPrice(parse.getDataByURL(
                             config.filter_params_dict[call.data])), parse_mode='HTML')
    elif call.data == 'price_graph':
        bot.send_message(call.message.chat.id,
                         'График цен за последнию неделю', reply_markup=start)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


try:
    bot.infinity_polling(True)
except Exception as bot_polling_error:
    print(bot_polling_error)
