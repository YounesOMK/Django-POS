from .base import *


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SOL_SECRET_KEY')

STATIC_ROOT = [
    BASE_DIR / 'staticfiles'
]