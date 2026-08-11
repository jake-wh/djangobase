from .base import *
environ.Env.read_env(
    env_file=BASE_DIR / '.env/env_local'
)
# ----------------------------------------

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

