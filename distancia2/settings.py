"""
Django settings for distancia2 project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

env = environ.Env()
env.read_env('distancia2/devel.env')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = environ.Path(__file__) - 2


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY',
    default='z5q$4jn)0k=3l_mefx9re*g#@1g@$y6y^yr*xf0sa6+4%xol!*')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True)

if DEBUG:
    ALLOWED_HOSTS = ['*']
    CORS_ORIGIN_ALLOW_ALL = True
else:
    ALLOWED_HOSTS = ['.distancia2.com']
    CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?distancia2\.com$', )


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'corsheaders',
    'rest_framework',
    'django_extensions',

    # Internal apps
    'cams.apps.CamsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'distancia2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'distancia2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': env('MYSQL_DATABASE'),
        'USER': env('MYSQL_USERNAME'),
        'PASSWORD': env('MYSQL_PASSWORD'),
    }
}


REDIS_HOST = env('REDIS_HOST')
REDIS_DATABASE = env.int('REDIS_DATABASE')
REDIS_USERNAME = env('REDIS_USERNAME')
REDIS_PASSWORD = env('REDIS_PASSWORD')


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0', 
    '--allow-root',
    '--no-browser', 
]


MODEL_PATH = env('MODEL_PATH')
MODEL_NAMES = env('MODEL_NAMES')
MODEL_WEIGHTS = env('MODEL_WEIGHTS')
MODEL_CONFIG = env('MODEL_CONFIG')
MODEL_ENABLE_CUDA = env.bool('MODEL_ENABLE_CUDA')
MODEL_CONFIDENCE = env.float('MODEL_CONFIDENCE')
MODEL_THRESHOLD = env.float('MODEL_THRESHOLD')
MODEL_PEOPLE_HEIGHT = env.float('MODEL_PEOPLE_HEIGHT')
