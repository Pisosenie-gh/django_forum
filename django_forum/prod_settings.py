from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'y&@7_6xr$xkj+weqwewqeqwwx=dz$p4g^8-+p5t#@flyjlwer&+vx2i)'


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'forum',
        'USER': 'user_db',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR , 'static')
