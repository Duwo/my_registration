"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SITE_ID = 1
SECRET_KEY = os.environ.get('ACCOUNTS_SECRET_KEY')
if  os.environ.get('DEBUG') == "True":
  DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# DATABASE_ROUTERS = [ "mysite.db_router.AuthRouter"]
DATABASES = {
    'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': os.environ.get("ACCOUNTS_DB"),       
          'USER': os.environ.get("ACCOUNTS_POSTGRES_USER"),
          'PASSWORD': os.environ.get("ACCOUNTS_POSTGRES_PASSWORD"),
          'HOST': os.environ.get("ACCOUNTS_POSTGRES_ADDR"),
          'PORT': os.environ.get("ACCOUNTS_POSTGRES_PORT"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "bower_components/")
]

if  os.environ.get('DEBUG') != "True":
  STATIC_URL = "https://dl.dropboxusercontent.com/u/29474323/accounts_static/"
else:
  STATIC_URL = "/accounts_static/"

STATIC_ROOT = "/accounts_static/"
MEDIA_URL = "/accounts_media/"
MEDIA_ROOT = "/accounts_media/"
LOGIN_REDIRECT_URL = '/accounts/profile'

if os.environ.get('DJANGO_ENV') == "test":
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
  }

  STATIC_URL = "/polls_static/"
  STATIC_ROOT = os.path.join(BASE_DIR, "polls_static/")
  MEDIA_URL = "/polls_media/"
  MEDIA_ROOT = os.path.join(BASE_DIR, "polls_media/")
