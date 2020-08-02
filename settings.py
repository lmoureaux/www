import json
import os

DEBUG = os.environ.get('LONGTURN_DEBUG', True)
SECRET_KEY = os.environ['LONGTURN_SECRET_KEY']

ADMINS = (
	('Michal Mazurek', 'akfaew@gmail.com'),
)

MANAGERS = ADMINS

# DATABASES from databases.json
DATABASES = json.load(open(os.environ.get('LONGTURN_DATABASES', 'databases.json'), 'r'))

APPEND_SLASH = True
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
LANGUAGES = [
		('en-us', 'English'),
	]
USE_L10N = False
MEDIA_ROOT = '/home/longturn-www/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/longturn-www/longturn/static/'
STATIC_URL = '/static/'
PLOT_PATH = '/home/longturn-www/longturn/plots/'
ADMIN_MEDIA_PREFIX = '/media/'
# SECRET_KEY from settings_secret

MIDDLEWARE = (
	'django.middleware.common.CommonMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
	'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'longturn.urls'

#ALLOWED_HOSTS = ['localhost']
ALLOWED_HOSTS = ['longturn.net', 'www.longturn.net']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
#            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.request',
            'django.template.context_processors.static',
#            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            'longturn.main.models.paths',
            'longturn.main.models.active_games',
            'sekizai.context_processors.sekizai',
            'cms.context_processors.cms_settings',
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
#           'django.template.loaders.app_directories.load_template_source',
#           'django.template.loaders.eggs.Loader',
        ]
    },
    'DIRS': [
        './longturn/templates',
	'/home/longturn-www/longturn/templates',
    ]
}]

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.humanize',
	'longturn.main',
	'longturn.player',
	'longturn.game',
	'longturn.warcalc',
	'longturn.serv',
	'longturn.fluxbb',
	'longturn.old',
	'sekizai',
	'cms',
	'menus',
	'treebeard',
	'filer',
	'easy_thumbnails',
	'mptt',
	'djangocms_text_ckeditor',
	'djangocms_link',
	'djangocms_file',
	'djangocms_picture',
	'djangocms_video',
	'djangocms_googlemap',
	'djangocms_snippet',
	'djangocms_style',
)
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
CMS_TEMPLATES = [
    ('cms.html', 'Home page template'),
]
CMS_PLACEHOLDER_CONF = {}

LOGIN_URL = "/account/login/"
LOGIN_REDIRECT_URL = "/account/profile/"

AUTHENTICATION_BACKENDS = ('longturn.player.backends.GenMD5ModelBackend',)
