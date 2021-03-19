from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'y&@7_6xr$xkj+wfrwwx=dz$p4g^8-+p5t#@flyjlwer&+vx2i)'

DEBUG = True

ALLOWED_HOSTS = ['8t-corporation.com', '185.5.206.68']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'forum',
        'USER': 'user_db',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '',

    }
}





STATIC_ROOT = os.path.join(BASE_DIR , 'static')

