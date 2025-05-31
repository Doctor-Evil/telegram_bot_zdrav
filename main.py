from config import settings
from google import genai

import telebot

client = genai.Client(api_key=settings.GEMINI_API_KEY)
bot = telebot.TeleBot(settings.TOKEN_TELEGRAM)

@bot.message_handler(commands=['start'])
def start_command(message):
    print(f"Received /start command from {message.from_user.username}")
    bot.send_message(message.chat.id, "Hello! I'm your bot. How can I assist you today?")

@bot.message_handler(content_types=['text'])
def text_command(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=message.text
    )
    bot.send_message(message.chat.id, f"You said: {message.text}")
    bot.send_message(message.chat.id, f"Response from Gemini: {response.text}")

if __name__ == "__main__":
    print("Bot is starting...")
    bot.polling(none_stop=True)