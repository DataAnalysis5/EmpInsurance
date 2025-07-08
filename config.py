import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_super_secret_key')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongo:27017/')
    WTF_CSRF_ENABLED = True
