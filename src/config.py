import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-api-key')
