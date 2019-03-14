from .base import *
from configparser import RawConfigParser

config = RawConfigParser()
config.read(os.path.join(BASE_DIR, "ares/settings/dev.ini"))

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'ENGINE'),
        'NAME': config.get('database', 'NAME'),
        'USER': config.get('database', 'USER'),
        'PASSWORD': config.get('database', 'PASSWORD'),
        'HOST': config.get('database', 'HOST'),
        'PORT': config.get('database', 'PORT')
    }
}
