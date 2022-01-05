"""
Django settings for guess_movie project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
import logging

IS_PROD = os.environ['IS_PROD']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

if IS_PROD == 'True':
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if IS_PROD == 'True':
    DEBUG = False
else:
    DEBUG = True

if IS_PROD == 'True':
    ALLOWED_HOSTS = ['movizz.fr', '51.68.225.98']
else:
    ALLOWED_HOSTS = []


if IS_PROD == 'True':
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"level": "INFO", "handlers": ["file"]},
        "handlers": {
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": "/home/tanguy/logs/django.log",
                "formatter": "app",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": True
            },
        },
        "formatters": {
            "app": {
                "format": (
                    u"%(asctime)s [%(levelname)-8s] "
                    "(%(module)s.%(funcName)s) %(message)s"
                ),
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
    }

# Application definition

INSTALLED_APPS = [
    'quizz.apps.QuizzConfig',
    'lyrizz.apps.LyrizzConfig',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'django_extensions'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'guess_movie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'guess_movie.wsgi.application'

# Channels
ASGI_APPLICATION = 'guess_movie.asgi.application'

if IS_PROD == 'True':
    # ipadress = '51.68.225.98'
    ipadress = 'redis://:george_abitbol@51.68.225.98:6379'
else:
    # ipadress = '127.0.0.1'
    ipadress = 'redis://127.0.0.1:6379'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            # "hosts": [(ipadress, 6379)],
            "hosts": [(ipadress)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

if IS_PROD == 'True':
    mysql_file = 'mysql_prod.cnf'
else:
    mysql_file = 'mysql.cnf'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, mysql_file),
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AUTHENTICATION_BACKENDS = [
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',
#
#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]
#
SITE_ID = 1
#
# # Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     # 'google': {
#     #     # For each OAuth based provider, either add a ``SocialApp``
#     #     # (``socialaccount`` app) containing the required client
#     #     # credentials, or list them here:
#     #     'APP': {
#     #         'client_id': '123',
#     #         'secret': '456',
#     #         'key': ''
#     #     }
#     # }
# }

LOGIN_REDIRECT_URL = '/quizz/'
# LOGIN_URL = ''

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'quizz', 'static'),
    ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA_ROOT = '/home/tanguy/workspace/git/guess_movie/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'
