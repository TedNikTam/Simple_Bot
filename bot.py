import telebot

bot = telebot.TeleBot('7016733305:AAES3DPE1D0QuUbzkQtkXz8IazclmxwqymU')


@bot.message_handler(commands=['start'])
def start(message):
    # создается таблица в базе и запрашивается отписание задачи
        bot.send_message(message.chat.id, 'Привет')

bot.polling(non_stop=True)