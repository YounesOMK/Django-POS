from .base import * 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y#lbo(slbb7pj02x9g=ir(t_h*8j%ruflu$v@h4tx!%rs=i11e"


INSTALLED_APPS += [
    'debug_toolbar',
    'django_browser_reload',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

STATICFILES_DIRS = [
    APPS_DIR / 'theme' / 'static'
]


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'