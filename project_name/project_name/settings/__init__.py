# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)
import os, pwd


# https://code.djangoproject.com/wiki/SplitSettings#SettingInheritancewithHierarchy
DEFAULT = 'common'


INSTALLED_APPS = ()


# certain keys we want to merge instead of copy
merge_keys = ('INSTALLED_APPS', 'MIDDLEWARE_CLASSES', 'ALLOWED_HOSTS')

def deep_update(from_dict, to_dict):
    """ i dont know, taken from https://code.djangoproject.com/wiki/SplitSettings#SettingInheritancewithHierarchy"""
    for (key, value) in from_dict.iteritems():
        if key in to_dict.keys() and isinstance(to_dict[key], dict) and isinstance(value, dict):
            deep_update(value, to_dict[key])
        elif key in merge_keys:
            if not key in to_dict:
                to_dict[key] = ()
            to_dict[key] = from_dict[key] + to_dict[key]
        else:
            to_dict[key] = value

# this should be one of prod, qa, staging, dev. Default to dev for safety.
env = os.environ.get('APP_SETTINGS', False)
users_settings = ''

modules = [DEFAULT]
if env:
    modules.append(env)
    modules.append(env+"_custom")
else:
    # try to load user specific settings
    users_settings = os.path.join("users", pwd.getpwuid(os.getuid())[0])
    modules.append(users_settings)


current = __name__
for module_name in modules:
    try:
        module = getattr(__import__(current, globals(), locals(), [module_name]), module_name)
    except ImportError, e:
        logger.exception('Unable to import {0} configuration: {1}'.format(module_name, e))
        raise
    except AttributeError, e:
        if module_name == users_settings:
            logger.debug("user settings not found or error loading it")
        elif env and module_name == env+"_custom":
            logger.debug("custom env settings not found or error loading it")
        else:
            logger.warning("No specific settings found")
        continue

    # create a local copy of this module's settings
    module_settings = {}
    for setting in dir(module):
        # all django settings are uppercase, so this ensures we
        # are only processing settings from the dir() call
        if setting == setting.upper():
            module_settings[setting] = getattr(module, setting)
    deep_update(module_settings, locals())
