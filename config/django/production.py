from .base import *
import dj_database_url
environ.Env.read_env(
    env_file=BASE_DIR / '.env/env_production'
)
# ----------------------------------------

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.parse(
        env('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True
    )
}
