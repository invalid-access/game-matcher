"""Production settings and globals."""
import redis
from os import environ

from settings import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

########## GENERAL CONFIGURATION
def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.oorjan.com',
    'game-matcher.herokuapp.com'
]
########## END GENERAL CONFIGURATION


########## ALL-IMPORTANT PATCH PSYCOPG
from psycogreen.gevent import patch_psycopg
patch_psycopg()
########## END ALL-IMPORTANT PATCH PSYCOPG

########## HEROKU DATABASE CONFIGURATION
import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
########## END HEROKU DATABASE CONFIGURATION



########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

########## END STATIC FILE CONFIGURATION
