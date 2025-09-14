from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4dsx-s8fcqunc%gt60cz2g6tz&r^8-rzbux*^&)-s@6ee_tacs'

DEBUG = True
ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# ✅ Only essential apps — no DB, no auth, no admin
INSTALLED_APPS = [
    'django.contrib.admin',         # ✅ Needed for admin panel
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Fort',  # your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',       # ✅ Must come before AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    # ✅ Required for admin and auth
    'django.contrib.messages.middleware.MessageMiddleware',       # ✅ Required for messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'loginmod.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # or [os.path.join(BASE_DIR, 'templates')] if you have custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',         # ✅ required for admin
                'django.contrib.messages.context_processors.messages', # ✅ required for messages
            ],
        },
    },
]


WSGI_APPLICATION = 'loginmod.wsgi.application'

# ❌ No database needed
#DATABASES = {
  #'default': {
   #'ENGINE': 'django.db.backends.dummy',
    # }
#}

# ✅ Remove password validators (not needed)
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
