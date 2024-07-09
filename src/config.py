import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key_example')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'openai_api_key_example')
    OPENAI_ORGANIZATION_ID = os.getenv('OPENAI_ORGANIZATION_ID', 'openai_organization_id_example')
