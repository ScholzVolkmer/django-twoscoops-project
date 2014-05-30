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
    'djangocms_admin_style',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'south',
    'pipeline',
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'reversion',
    'djangocms_text_ckeditor',
    'django_extensions',
    #'djangocms_teaser',
    #'djangocms_inherit',
    #'djangocms_picture',
    #'djangocms_video',
    #'djangocms_link',
    'filer',
    'easy_thumbnails',
    #'cmsplugin_filer_file',
    #'cmsplugin_filer_folder',
    #'cmsplugin_filer_image',
    #'cmsplugin_filer_teaser',
    #'cmsplugin_filer_video',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'application',
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
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
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
            'level': 'ERROR',
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
PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_YUI_BINARY = '/usr/bin/env yui-compressor'
# uncomment when the app created
PIPELINE_CSS = {
    'application': {
        'source_filenames': (
            'sass/main.sass',
        ),
        'output_filename': 'main.css',
    },
}
PIPELINE_JS = {
    'application': {
        'source_filenames': (
            'coffee/second.coffee',
            'coffee/main.coffee',
        ),
        'output_filename': 'main.js',
    },
}

PIPELINE_COFFEE_SCRIPT_ARGUMENTS = "-b"
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_ALIASES_ORDER = ['default', ]
SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}

TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
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
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)
CMS_TEMPLATES = (
    ('base.html', 'Base Template'),
)

TEST_DISCOVERY_ROOT = os.path.join(PROJECT_DIR, "tests")
TEST_RUNNER = "tests.runner.DiscoveryRunner"

# THIS SHOULD BE THE LAST ENTRY IN settings.py
# THIS OVERRIDES SETTINGS IF WE ARE RUNNING TESTS
if 'test' in sys.argv or 'jenkins' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'mb_com.sqlite'}
    SOUTH_TESTS_MIGRATE = False
