import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN", "8675404338:AAE_4FEe2L0GoyeoAu6AhsTgMMDBAlF-YtM")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Бот работает на Render 24/7!")

print("Бот запущен!")
bot.infinity_polling()
