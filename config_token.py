import os
from dotenv import load_dotenv

load_dotenv()
telegram_api_token = os.getenv('TELEGRAM_API_TOKEN')

if telegram_api_token is None:
    raise ValueError('Переменная окружения не установлена')

print(f'\nOur token on Telegram Bot: {telegram_api_token}')