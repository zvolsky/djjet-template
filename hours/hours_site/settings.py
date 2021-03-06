"""
Django settings for hours_site project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

from decouple import config, Csv   # python-decouple (.env)
from dj_database_url import parse as db_url  # for python-decouple/.env DATABASE setting
from unipath import Path


JET = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_generate_secret_key',
    'django_smoke_tests',
]
if JET:
    INSTALLED_APPS.insert(0, 'jet')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hours_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hours_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': config(
        'DB_URL',
        default='sqlite:///' + BASE_DIR.child('%s.sqlite3' % BASE_DIR.stem),
        cast=db_url
    )
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Prague'  # default: 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# -------------------------------------------------------------------------------

if JET:
    # JET
    JET_SIDE_MENU_COMPACT = True

    ''' # musí souhlasit počet s admin.py registrací !!!
    JET_SIDE_MENU_ITEMS = [
        {'app_label': 'auth', 'items': [
            {'name': 'group'},
            {'name': 'user'},
        ]},
        {'app_label': 'academic', 'items': [
            {'name': 'branch'},
            {'name': 'industry'},
            {'name': 'institute'},
            {'name': 'offer'},
            {'name': 'person'},
            {'name': 'product'},
            {'name': 'team'},
            {'name': 'x_product_author'},
            {'name': 'x_product_branch'},
            {'name': 'x_product_offer'},
            {'name': 'x_product_team'},
            {'name': 'x_team_author'},
        ]},
        {'app_label': 'boards', 'items': [
            {'name': 'board'},
            {'name': 'topic'},
            {'name': 'post'},
        ]},
    ]
    '''

    JET_THEMES = [
        {
            'theme': 'default', # theme folder name
            'color': '#47bac1', # color of the theme's button in user menu
            'title': 'Default' # theme title
        },
        {
            'theme': 'green',
            'color': '#44b78b',
            'title': 'Green'
        },
        {
            'theme': 'light-gray',
            'color': '#222',
            'title': 'Light Gray'
        }
    ]
    '''
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    '''
