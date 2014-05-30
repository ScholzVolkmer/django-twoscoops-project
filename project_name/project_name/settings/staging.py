SITE_ID = 3
DEBUG = False
ALLOWED_HOSTS = ("staging",)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'staging',
        'USER': 'staging',
        'PASSWORD': 'XXX',
        'HOST': ''
    }
}
