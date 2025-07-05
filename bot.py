import telebot
import os

# Initialize the bot with your Telegram Bot Token
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your automated Telegram bot. How can I assist you today?")

# Define a handler for all text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot
if __name__ == "__main__":
    bot.polling()