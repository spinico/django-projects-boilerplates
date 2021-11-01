"""
Django project settings.
"""

import os
import sys


def gettext(s):
    return s


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BACKEND_DIR = os.path.realpath(BASE_DIR)

APPS_DIR = os.path.realpath(os.path.join(BACKEND_DIR, 'apps'))
sys.path.append(APPS_DIR)

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# By default, do not include the debug toolbar (True in development settings)
DEBUG_TOOLBAR = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_simple_cookie_consent',
    'corsheaders',
    'analytical',
    'demo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

# If True, the whitelist will not be used and all origins will be accepted. Defaults to False.
CORS_ORIGIN_ALLOW_ALL = True
# If True, cookies will be allowed to be included in cross-site HTTP requests. Defaults to False.
CORS_ALLOW_CREDENTIALS = True
# A list of origins that are authorized to make cross-site HTTP requests. Defaults to [].
CORS_ORIGIN_WHITELIST = []


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


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BACKEND_DIR, 'db.sqlite3'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Translations

LANGUAGES = (
    # Customize this
    ('en', gettext('English')),
)

# Logging

LOGS_ROOT = os.path.realpath(os.path.join(BACKEND_DIR, 'logs'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_format': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file_format': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console_format',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, 'django.log'),
            'maxBytes': 1024 * 1024 * 15,  # 15 MB
            'backupCount': 10,
            'formatter': 'file_format',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        # Remark: applications logger's module name should have the 'apps.' prefix
        'apps': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # Default error sink logger
        '': {
            'level': 'ERROR',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
}

# Static files (CSS, JavaScript, Images)

STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')

# Url that handles the static files served from STATIC_ROOT.
# Use a trailing slash '/' if there is a path component (optional in other cases)
STATIC_URL = STATIC_HOST + '/static/'

# Absolute path to the directory where Django static files are collected
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# List of directories were to find static assets
STATICFILES_DIRS = [
    os.path.join(BACKEND_DIR, 'build'),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Url that handles the media served from MEDIA_ROOT.
# Use a trailing slash '/' if there is a path component (optional in other cases)
# In production, uploaded files should be served from a different domain
# Note: the media url cannot be located within the static url
MEDIA_URL = 'https://media.example.com/'

# Absolute path to the directory that will hold user-uploaded files
# Note: by default, Django doesn't serve media files during development (i.e. when debug=True)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Django Analytical

# CHARTBEAT_USER_ID = '12345'
# CLICKMAP_TRACKER_CODE = '12345678....912'
# CLICKY_SITE_ID = '12345678'
# CRAZY_EGG_ACCOUNT_NUMBER = '12345678'
# FACEBOOK_PIXEL_ID = '1234567890'
# GAUGES_SITE_ID = '0123456789abcdef0123456789abcdef'
# GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-1234567-8'
# HUBSPOT_PORTAL_ID = '1234'
# HUBSPOT_DOMAIN = 'somedomain.web101.hubspot.com'
# INTERCOM_APP_ID = '0123456789abcdef0123456789abcdef01234567'
# KISS_INSIGHTS_ACCOUNT_NUMBER = '12345'
# KISS_INSIGHTS_SITE_CODE = 'abc'
# KISS_METRICS_API_KEY = '0123456789abcdef0123456789abcdef01234567'
# MIXPANEL_API_TOKEN = '0123456789abcdef0123456789abcdef'
# OLARK_SITE_ID = '1234-567-89-0123'
# OPTIMIZELY_ACCOUNT_NUMBER = '1234567'
# PERFORMABLE_API_KEY = '123abc'
# PIWIK_DOMAIN_PATH = 'your.piwik.server/optional/path'
# PIWIK_SITE_ID = '123'
# RATING_MAILRU_COUNTER_ID = '1234567'
# WOOPRA_DOMAIN = 'abcde.com'
# YANDEX_METRICA_COUNTER_ID = '12345678'
