# -*- coding: utf-8 -*-

import telebot
import re
from telebot import types

token = '769918614:AAGJTSc4pHSrAfuzbmKnoNaV2fD8U2OUyx8'
bot = telebot.TeleBot(token)

#https://api.telegram.org/file/bot769918614:AAGJTSc4pHSrAfuzbmKnoNaV2fD8U2OUyx8/voice/file_0.oga
@bot.inline_handler(func=lambda query: len(query.query) is 0)
def empty_query(query):
    try:
        r1 = types.InlineQueryResultCachedVoice(
                id='31',
                voice_file_id="AwADAgADTgIAAgQyYUpe6eFUcHwcBwI",
                parse_mode='Markdown',
                title="Результат 1:"
        )
        r2 = types.InlineQueryResultCachedVoice(
                id='32',
                voice_file_id="AwADAgADTwIAAgQyYUrPbCec1P3QtgI",
                parse_mode='Markdown',
                title="Результат 2:"
        )
        r3 = types.InlineQueryResultCachedVoice(
                id='33',
                voice_file_id="AwADAgADUAIAAgQyYUreWs-vaDmuAgI",
                parse_mode='Markdown',
                title="Результат 3:"
        )
        bot.answer_inline_query(query.id, [r1, r2, r3])
    except Exception as e:
        print(e)

if __name__ == '__main__':
     bot.polling(none_stop=True)
