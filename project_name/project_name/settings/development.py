SITE_ID = 1
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{project_name}}',
        'USER': '{{project_name}}',
        'PASSWORD': 'password',
        'HOST': ''
    }
}
