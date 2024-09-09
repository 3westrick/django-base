from .settings import *

if os.getenv('DATABASE') == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': os.getenv('HOST'),
            'POST': 5432,
        }
    }

