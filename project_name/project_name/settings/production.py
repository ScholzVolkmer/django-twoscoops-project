SITE_ID = 2
DEBUG = False
ALLOWED_HOSTS = ("production",)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'production',
        'USER': 'production',
        'PASSWORD': 'XXX',
        'HOST': ''
    }
}
INSTALLED_APPS = (
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': 'your_raven_DSN',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s',
        },
        'simple': {
            'format': '>>> %(levelname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.db': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'raven.errors': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
        },
        'requests': {
            'level': 'WARNING',
            'handlers': ['console', 'sentry'],
        },
        '': {
            'handlers': ['console', 'sentry'],
            'level': 'WARNING',
        },
    },
}
