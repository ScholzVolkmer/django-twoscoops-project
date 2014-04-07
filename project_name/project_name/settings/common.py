# -*- coding: utf-8 -*- #pylint: disable-msg=C0302
import os
import sys
from django.utils.translation import ugettext_lazy as _
from sys import path

ugettext = lambda s: s

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = os.path.dirname(PROJECT_DIR)

# Site name:
SITE_NAME = os.path.basename(PROJECT_DIR)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(PROJECT_DIR)
########## END PATH CONFIGURATION

SITE_ID = 1

CONFIGURATION = 'common'  # what configuration is this

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SECRET_KEY = r"{{ secret_key }}"

ROOT_URLCONF = '%s.urls' % SITE_NAME

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'south',
    'filer',
    'pipeline',
    'easy_thumbnails',
)

# Apps specific for this project go here.
LOCAL_APPS = (
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION

########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = (
    'localhost',
    '127.0.0.1',
)
########## END SITE CONFIGURATION

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': SITE_NAME + CONFIGURATION
    }
}

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 2
CACHE_MIDDLEWARE_KEY_PREFIX = ""
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_TEMPLATE_TIMEOUT = 60

DEBUG = True

TEMPLATE_DEBUG = DEBUG

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s  %(message)s',
            'datefmt': '%y %b %d, %H:%M:%S',
        },
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'log_to_stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, os.pardir, "logs", SITE_NAME + ".log"),
            'maxBytes': 500000,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'tests.data': {
            'handlers': ['log_to_stdout'],
            'level': 'INFO',
        }
    }

}

EMAIL_HOST = 'localhost'
TIME_ZONE = 'Europe/Berlin'
LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale'),
)
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
)
DEFAULT_LANGUAGE = 0
USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_DISABLE_WRAPPER = True
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE_STORAGE = 'pipeline.storage.PipelineFinderStorage'

PIPELINE_JS = {
    # 'head_ie': {
    #     'source_filenames': (
    #         'assets/javascripts/vendor/selectivzr-1.0.2.js',
    #     ),
    #     'output_filename': 'assets/javascripts/head_ie.min.js',
    # },
    'head': {
        'source_filenames': (
            'assets/javascripts/vendor/modernizr-2.6.2.js',
            #'assets/javascripts/vendor/selectivizr.js',
        ),
        'output_filename': 'assets/javascripts/head.min.js',
    },

    'jquery': {
        'source_filenames': (
            'assets/javascripts/vendor/jquery-2.0.3.js',
        ),
        'output_filename': 'assets/javascripts/jquery.min.js',
    },

    'jquery_ie': {
        'source_filenames': (
            'assets/javascripts/vendor/jquery-1.10.2.js',
        ),
        'output_filename': 'assets/javascripts/jquery.ie.min.js',
    },

    'application': {
        'source_filenames': (
            'assets/javascripts/vendor/TweenMax-1.10.3.js',
            'assets/javascripts/vendor/plugins/*',
            'assets/javascripts/application/core.js',
            'assets/javascripts/application/helpers.js',
            'assets/javascripts/application/loader.js',
            'assets/javascripts/application/loader.jPreload.js',
            'assets/javascripts/application/log.js',
            'assets/javascripts/application/layout.js',
            'assets/javascripts/application/plugins.js',
            'assets/javascripts/application/plugins/*',
            #'assets/javascripts/application/deeplink.js',
            #'assets/javascripts/plugins/wordwrap.js',
        ),
        'output_filename': 'assets/javascripts/application.min.js',
    }
}

PIPELINE_CSS = {
    'ie': {
        'source_filenames': (
            'assets/stylesheets/css/ie.css',
        ),
        'output_filename': 'assets/stylesheets/css/ie.min.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'screen': {
        'source_filenames': (
            'assets/stylesheets/css/screen.css',
        ),
        'output_filename': 'assets/stylesheets/css/screen.min.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    },
    'print': {
        'source_filenames': (
            'assets/stylesheets/css/print.css',
        ),
        'output_filename': 'assets/stylesheets/css/print.min.css',
        'extra_context': {
            'media': 'print, embossed',
        },
    }
}

FILER_FILE_MODELS = (
    "core.models.Video",
    "core.models.Document",
    "core.models.Audio",
    "core.models.Image",
    "core.models.UndefinedMedia"
)

FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'UPLOAD_TO': 'filer.utils.generate_filename.by_date'
        },
        'download': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
        },
    },
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_ALIASES_ORDER = ['default', ]

THUMBNAIL_ALIASES = {
    'default': {
        'slider': {
            'title': _('Slider Background'),
            'size': (1280, 496),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'slider_gallery': {
            'title': _('Slider Gallery'),
            'size': (1280, 600),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'slider_thumb': {
            'title': _('Slider Background Thumb'),
            'size': (146, 82),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'slider_article': {
            'title': _('Slider Background Article'),
            'size': (666, 374),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'slider_article_portrait': {
            'title': _('Slider Background Portrait'),
            'size': (666, 0),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_article': {
            'title': _('Teaser Article/Video/Gallery'),
            'size': (312, 176),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_article_share': {
            'title': _('Teaser Article/Video/Gallery'),
            'size': (400, 209),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'textImage_article': {
            'title': _('TextImage Article'),
            'size': (252, 190),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_social': {
            'title': _('Teaser Social '),
            'size': (312, 205),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_static_1x1': {
            'title': _('Teaser Static 1x1'),
            'size': (312, 260),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_static_1x2': {
            'title': _('Teaser Static 1x2'),
            'size': (312, 390),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_static_1x2_mobile': {
            'title': _('Teaser Static 1x2 Mobile'),
            'size': (278, 202),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_static_2x1': {
            'title': _('Teaser Static 2x1'),
            'size': (630, 260),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_heritage': {
            'title': _('Teaser Heritage'),
            'size': (312, 205),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'teaser_horizontal_aside': {
            'title': _('Teaser Aside in Detail View'),
            'size': (155, 87),
            'autocrop': False,
            'crop': 'smart',
            'upscale': False,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'partner_footer': {
            'title': _('Partner Footer'),
            'size': (252, 152),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'partner_footer_large': {
            'title': _('Partner Footer Large'),
            'size': (244, 420),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'partner_footer_wide': {
            'title': _('Partner Footer Large'),
            'size': (341, 207),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
        'track': {
            'title': _('track'),
            'size': (1280, 500),
            'autocrop': False,
            'crop': 'smart',
            'upscale': True,
            'preview': True,
            'mask': '0 3px 0 3px',
        },
    },
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

TEST_DISCOVERY_ROOT = os.path.join(PROJECT_DIR, "tests")
TEST_RUNNER = "tests.runner.DiscoveryRunner"

# THIS SHOULD BE THE LAST ENTRY IN settings.py
# THIS OVERRIDES SETTINGS IF WE ARE RUNNING TESTS
if 'test' in sys.argv or 'jenkins' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'mb_com.sqlite'}
    SOUTH_TESTS_MIGRATE = False
