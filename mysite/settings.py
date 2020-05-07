"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import django_heroku
from os import environ
# GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal300'
# django_heroku.settings(locals())
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@z5u7y2thz#)4=s!tg33_)1sc#qpx5rzr-mpcfoea*we&n1c9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'yasser-city-tracker.herokuapp.com',
    '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'maps',
    'django.contrib.gis',
    'djgeojson'
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
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE' : 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geolocations',
        'USER': 'postgres',
        'PASSWORD': 'Yoznob99!!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['ENGINE'] = "django.contrib.gis.db.backends.postgis"

# GEOS_LIBRARY_PATH = '/app/.geodjango/geos/lib/libgeos_c.so'
#
# GDAL_LIBRARY_PATH = '/app/.geodjango/gdal/lib/libgdal.so'
#help me god

_GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH', None)
if _GDAL_LIBRARY_PATH:
    GDAL_LIBRARY_PATH = _GDAL_LIBRARY_PATH
_GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH', None)
if _GEOS_LIBRARY_PATH:
    GEOS_LIBRARY_PATH = _GEOS_LIBRARY_PATH

# DATABASES['default] = {default': dj_database_url.config()}
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
# DATABASES['default'] = dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# DATABASES['default'] =  dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
# GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
# GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

# GEOS_LIBRARY_PATH = os.environ['GEOS_LIBRARY_PATH']
#
# GDAL_LIBRARY_PATH = os.environ['GDAL_LIBRARY_PATH']
# PROJ4_LIBRARY_PATH = os.environ['PROJ4_LIBRARY_PATH']


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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
django_heroku.settings(locals())