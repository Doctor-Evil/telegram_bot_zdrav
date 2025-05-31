from config import settings

import telebot

bot = telebot.TeleBot(settings.telegram_token)

@bot.message_handler(commands=['start'])
def start_command(message):
    print(f"Received /start command from {message.from_user.username}")
    bot.send_message(message.chat.id, "Hello! I'm your bot. How can I assist you today?")

if __name__ == "__main__":
    print("Bot is starting...")
    bot.polling(none_stop=True)