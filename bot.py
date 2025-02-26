import telebot

TOKEN = "7386138034:AAFW2feaCJZph6hrQ43SAnR_c0t0eLXWXis"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Salom! Bot ishga tushdi.")

bot.polling()