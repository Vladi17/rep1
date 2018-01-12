 import asyncio
import aiohttp
from aiohttp import web
import json
   
async def init_app(loop):
    app = web.Application(loop=loop, middlewares=[])
    app.router.add_post('/api/v1', handler)
    return app	
app = loop.run_until_complete(init_app(loop))
web.run_app(app, host='0.0.0.0', port=23456)

import telebot
TOKEN = '427856651:AAFqImRn2q02LIw9eBlRrhHBiBbTNmnXw44'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)



    def hello(message):
        bot.send_message(message.chat.id,
 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

    bot.polling()