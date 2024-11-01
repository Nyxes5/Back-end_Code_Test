from .common import *

SECRET_KEY = 'django-insecure-ik2v!d3dub9v9_g=2&8+^zzkrc6kn&^1k-$okhm27d!h&-^^-%'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Used for simplicity and only in development
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}