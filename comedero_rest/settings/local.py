from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3307',
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'comedero',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': BASE_DIR / 'db.sqlite3',
#   }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'