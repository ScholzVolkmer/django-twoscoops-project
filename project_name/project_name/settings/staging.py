SITE_ID = 2
DEBUG = False
ALLOWED_HOSTS = ("staging",)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{project_name}}',
        'USER': '{{project_name}}',
        'PASSWORD': 'password',
        'HOST': ''
    }
}
