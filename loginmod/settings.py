from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4dsx-s8fcqunc%gt60cz2g6tz&r^8-rzbux*^&)-s@6ee_tacs'

DEBUG = True
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# ✅ Only essential apps — no DB, no auth, no admin
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'Fort',  # your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'loginmod.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'loginmod.wsgi.application'

# ❌ No database needed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

# ✅ Remove password validators (not needed)
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
