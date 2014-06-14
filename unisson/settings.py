# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
from django.utils.translation import gettext_lazy as _
PROJECT_DIR = os.path.dirname(__file__)
# Django settings for unisson project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Import settings for the given site
from site_settings import *

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),    
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, '..', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'static_prod'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, '..', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')tbe)ly!(5!lu2#^o0)tcy1jzmxz7rwa*=j6%9i-mt!bq^2b55'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'app_namespace.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',   
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
   # 'zinnia.context_processors.version',  # Optional
)

ROOT_URLCONF = 'unisson.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'unisson.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, '..', 'accounts/templates'),
    os.path.join(PROJECT_DIR, '..', 'templates'),
    os.path.join(PROJECT_DIR, '..', 'workgroup/templates'),
    os.path.join(PROJECT_DIR, '..', 'project/templates'),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'guardian',
    "django_extensions",
    'easy_thumbnails',
    'userena',
    'accounts',
    'social_auth',
    'djangocms_text_ckeditor',  # note this needs to be above the 'cms' entry
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'south',  # intelligent schema and data migrations
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list before 'django.contrib.admin'.
    'djangocms_video',
    'reversion',
    'tagging',
    'taggit',
    'mptt',
    'zinnia_bootstrap',
    'zinnia',
    'django_mailman',
    'workgroup',
    'project',
    'django.contrib.humanize',
    'django_notify',
    'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',
    'wiki.plugins.macros',
    'wiki.plugins.help',
    'wiki.plugins.links',
    'inplaceeditform',
    'inplaceeditform_extra_fields',
    'categories',
    'categories.editor',
 )

CKEDITOR_SETTINGS = {
    'toolbar': 'full',
}

INPLACEEDIT_EDIT_EMPTY_VALUE = 'Double click to edit'
INPLACEEDIT_AUTO_SAVE = True
INPLACEEDIT_EVENT = "dblclick"
INPLACEEDIT_DISABLE_CLICK = True  # For inplace edit text into a link tag
INPLACEEDIT_EDIT_MESSAGE_TRANSLATION = 'Write a translation' # transmeta option
INPLACEEDIT_SUCCESS_TEXT = 'Successfully saved'
INPLACEEDIT_UNSAVED_TEXT = 'You have unsaved changes'
INPLACE_ENABLE_CLASS = 'enable'
ADAPTOR_INPLACEEDIT_EDIT = 'inplaceeditform.perms.AdminDjangoPermEditInline'
DEFAULT_INPLACE_EDIT_OPTIONS = {} # dictionnary of the optionals parameters that the templatetag can receive to change its behavior (see the Advanced usage section)
DEFAULT_INPLACE_EDIT_OPTIONS_ONE_BY_ONE = True # modify the behavior of the DEFAULT_INPLACE_EDIT_OPTIONS usage, if True then it use the default values not specified in your template, if False it uses these options only when the dictionnary is empty (when you do put any options in your template)
INPLACE_GET_FIELD_URL = None # to change the url where django-inplaceedit use to get a field
INPLACE_SAVE_URL = None # to change the url where django-inplaceedit use to save a field

ADAPTOR_INPLACEEDIT = {'image': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
                       'fk': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteForeingKeyField',
                        'image_thumb': 'inplaceeditform_extra_fields.fields.AdaptorImageThumbnailField',
                       'm2mcomma': 'inplaceeditform_extra_fields.fields.AdaptorAutoCompleteManyToManyField'}

TEXT_ADDITIONAL_ATTRIBUTES = ('data-toggle', 'data-parent', 'original-title')

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleOAuthBackend',        
    'social_auth.backends.google.GoogleBackend',    
    'social_auth.backends.browserid.BrowserIDBackend',
    
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# USERENA
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/signin/'
LOGOUT_URL = '/signout/?next=/'
USERENA_DEFAULT_PRIVACY = 'open'
USERENA_MUGSHOT_SIZE = 120
USERENA_MUGSHOT_DEFAULT = 'monsterid'

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'accounts.Profile'


CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('projets.html', 'Projets'),
    ('home.html', 'Home'),
    ('contact.html', 'Contact'),
)

DEFAULT_FROM_EMAIL = 'contact@unisson.co'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

from django.core.urlresolvers import resolve, Resolver404, reverse_lazy
from django.http import Http404, HttpResponseRedirect, HttpResponse

def hacky_handle_no_page(request, slug):
    if not slug and DEBUG:
        return TemplateResponse(request, "cms/welcome.html", RequestContext(request))
    try:
        #add a $ to the end of the url (does not match on the cms anymore)
        resolve('%s$' % request.path)
    except Resolver404 as e:
        # raise a django http 404 page
        #exc = Http404(dict(path=request.path, tried=e.args[0]['tried']))
        exc = HttpResponseRedirect("/wiki/%s" % slug)
        return exc
    return HttpResponseRedirect("/wiki/%s" % slug)

import cms.views
cms.views._handle_no_page = hacky_handle_no_page

# South need the following lines for correct migrations handling.
# If not present, it raises a ImproperlyConfiguredError
# When launching `python manage.py migrate --fake`

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}