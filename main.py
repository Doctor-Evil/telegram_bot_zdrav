from config import settings
from google import genai

import json
import telebot

client = genai.Client(api_key=settings.GEMINI_API_KEY)
bot = telebot.TeleBot(settings.TOKEN_TELEGRAM)



def load_json():
    """Load JSON data from a file."""
    with open('staff.json', 'r', encoding='utf-8') as file:
        return json.load(file)

staff_info = load_json()

@bot.message_handler(commands=['start'])
def start_command(message):
    print(f"Received /start command from {message.from_user.username}")
    bot.send_message(message.chat.id, "Hello! I'm your bot. How can I assist you today?")

@bot.message_handler(content_types=['text'])
def text_command(message):
    prompt = f"""{message.text}\n\n{staff_info}\n\nНайди в этом тексте сотрудника и ответь на вопрос: {message.text}"""

    message_bot = bot.send_message(message.chat.id, "Бот думает...")
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    bot.delete_message(message.chat.id, message_bot.message_id)
    bot.send_message(message.chat.id, f"You said: {message.text}")

    print(f"{len(response.text)} characters received from Gemini.")
    print(f"Response from Gemini: {response.text}")
    
    bot.send_message(message.chat.id, f"Response from Gemini: {response.text[:4000]}")

if __name__ == "__main__":
    print("Bot is starting...")
    bot.polling(none_stop=True)