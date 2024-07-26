import os
from dotenv import load_dotenv

load_dotenv()


class AppConfig:
    def __init__(self):
        self.telegram_api_token = os.getenv('TELEGRAM_API_TOKEN')
        if self.telegram_api_token is None:
            raise ValueError('Переменная окружения не установлена')


conf = AppConfig()
print(f'\nOur token on Telegram Bot: {conf.telegram_api_token}')