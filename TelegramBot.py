import telebot

TOKEN = '498274738:AAHZgl5_SlX2i21JIQ-PyAXa86JLwDvcKgI'
bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop = False, interval = 0, timeout=20)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)