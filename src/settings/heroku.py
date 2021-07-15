"""
Production settings for heroku
"""

import environ

from src.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Parse database connection string
DATABASES = {
    'default': env.db()
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env('API_KEY'),
    'API_SECRET': env('API_SECRET'),
}