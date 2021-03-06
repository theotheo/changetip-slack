"""
Django settings for slack project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SLACK_CLIENT_ID = os.getenv("SLACK_CLIENT_ID", None)
SLACK_CLIENT_SECRET = os.getenv("SLACK_CLIENT_SECRET", None)
assert SLACK_CLIENT_ID, "Need to set SLACK_CLIENT_ID to run this app"
assert SLACK_CLIENT_SECRET, "Need to set SLACK_CLIENT_SECRET to run this app"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", 'ty9l!0q22*v(lo)9w*p#!iwbh4x3qz-1%^ixu1uz66y!bnykdv')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Hack to get admin errors logged locally. You can override with your own
ADMINS = (
    ('Test Account', 'dev@console.com'),
)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'slack'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

ROOT_URLCONF = 'slack.urls'

WSGI_APPLICATION = 'slack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bots',
        'USER': os.getenv('MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('MYSQL_PASS', ''),
        'HOST': os.getenv('MYSQL_HOST', 'localhost'),
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
