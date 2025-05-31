from config import settings

import telebot

bot = telebot.TeleBot(settings.telegram_token)

@bot.message_handler(commands=['start'])
def start_command(message):
    print(f"Received /start command from {message.from_user.username}")
    bot.send_message(message.chat.id, "Hello! I'm your bot. How can I assist you today?")

@bot.message_handler(content_types=['text'])
def text_command(message):
    print(f"Received /text command from {message.from_user.username}: {message.text}")
    bot.send_message(message.chat.id, f"You said: {message.text}")

if __name__ == "__main__":
    print("Bot is starting...")
    bot.polling(none_stop=True)