

from pathlib import Path
import django_heroku
import dj_database_url


import os
import dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)







BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY' 
SECURE_SSL_REDIRECT = True





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
# DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
DEBUG = False
ALLOWED_HOSTS = ['revolt-staging-7ab3e7777ea7.herokuapp.com','revolt-gallery-ecf8df9a70f7.herokuapp.com/','www.taosrevolt.com', 'taosrevolt.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'schedule',
    'django_celery_results',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
    
]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
ROOT_URLCONF = 'revolt_annex.urls'

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

WSGI_APPLICATION = 'revolt_annex.wsgi.app'
# WSGI_APPLICATION = 'revolt_annex.wsgi.application'

DATABASE_URL = str(os.getenv('DATABASE_URL'))
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': str(os.getenv('DB_NAME')),
        'USER': str(os.getenv('DB_USER')),
        'PASSWORD': str(os.getenv('DB_PASSWORD')),
        'HOST': str(os.getenv('DB_HOST')),
        'PORT': '5432',
    }
}



DATABASES['default'] = dj_database_url.config(
    default=str(os.getenv('DATABASE_URL')),
    conn_max_age=600,
    conn_health_checks=True,
)

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": "mydatabase",
#     }
# }

# DATABASE_ROUTERS = ['revolt_annex.database_router.AppBasedRouter']

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",
#     # ...
# ]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATE_INPUT_FORMATS = ["%m.%d.%Y"]
USE_L10N = False

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = {'application/json'}
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Paris'
CELERY_RESULT_BACKEND = 'django-db'


# Make sure the Celery Beat scheduler is enabled
CELERY_BEAT_SCHEDULER = 'celery.beat.PersistentScheduler'

# SMTP SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


EMAIL_HOST = str(os.getenv('MAILGUN_SMTP_SERVER')),
EMAIL_HOST_USER = str(os.getenv('MAILGUN_USER')), # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = str(os.getenv('MAILGUN_PASSWORD')),
EMAIL_PORT = os.getenv('MAILGUN_PORT'),
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = str(os.getenv('FROM_EMAIL')),


# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

