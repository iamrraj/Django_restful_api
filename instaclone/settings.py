"""
Django settings for instaclone project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4%ls$1((hv62760_humyq^=68qr5eo3!s8$@b7rp)+)c6j$&oh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jet.dashboard",
    "jet",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_rest_passwordreset',
    "cloudinary",
    "rest_framework",
    "drf_yasg",
    "tinymce",
    "django_filters",
    "oauth2_provider",
    "import_export",
    "taggit",
    "Post",
    'corsheaders',
    "user",
    "blog",
    "fcm_django",
    "data1"
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "user.middleware.UserActivityMiddleware",
]

ROOT_URLCONF = 'instaclone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "template")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'instaclone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    # 'DATETIME_FORMAT': "%Y-%m-%d",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}


MEDIA_ROOT = os.path.join(BASE_DIR, "images")

MEDIA_URL = "/media/"


STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"

AUTH_USER_MODEL = "user.User"

STATIC_DIRS = [os.path.join(BASE_DIR, "static")]

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


LOGOUT_URL = "/accounts/logout/"
LOGIN_REDIRECT_URL = "/swagger/"


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")



ACCESS_TOKEN_EXPIRE_SECONDS = 12 * 60 * 60  # Token wil expire in 12 hours

OAUTH2_PROVIDER = {
    "SCOPES": {"read": "Read scope", "write": "Write scope", },
    "CLIENT_ID_GENERATOR_CLASS": "oauth2_provider.generators.ClientIdGenerator",
    "ACCESS_TOKEN_EXPIRE_SECONDS": ACCESS_TOKEN_EXPIRE_SECONDS,
}


DJANGO_REST_PASSWORDRESET_IP_ADDRESS_HEADER = "HTTP_X_FORWARDED_FOR"
HTTP_USER_AGENT_HEADER = "HTTP_USER_AGENT"


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



TINYMCE_DEFAULT_CONFIG = {
    "cleanup_on_startup": True,
    "custom_undo_redo_levels": 20,
    "selector": "textarea",
    "theme": "modern",
    "width": 1000,
    "content_css": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
    "codesample_content_css": "http://ourcodeworld.com/material/css/prism.css",
    "codesample_dialog_height": 400,
    "codesample_dialog_width": 600,
    "codesample_languages": [
        {"text": "HTML/XML", "value": "markup"},
        {"text": "JavaScript", "value": "javascript"},
        {"text": "CSS", "value": "css"},
        {"text": "PHP", "value": "php"},
        {"text": "Ruby", "value": "ruby"},
        {"text": "Python", "value": "python"},
        {"text": "Java", "value": "java"},
        {"text": "C", "value": "c"},
        {"text": "C#", "value": "csharp"},
        {"text": "C++", "value": "cpp"},
    ],
    "plugins": """
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink   charmap print  hr
            anchor pagebreak spellchecker directionality paste searchreplace
            """,
    "toolbar1": """
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample 
            
            """,
    "toolbar2": """  
            searchreplace spellchecker paste save print | directionality
                """,
    "toolbar3": """
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code textcolor 
            """,
    "language": "{{ language }}",
    "directionality": "{{ directionality }}",
    "spellchecker_languages": "{{ spellchecker_languages }}",
    "spellchecker_rpc_url": "{{ spellchecker_rpc_url }}",
    "toolbar_sticky": True,
    "autosave_interval": "30s",
    "contextmenu": "formats | link image | codesample",
    "menubar": "file edit view insert format tools table help",
    "statusbar": True,
}


JET_THEMES = [
    {
        "theme": "default",  # theme folder name
        "color": "#47bac1",  # color of the theme's button in user menu
        "title": "Default",  # theme title
    },
    {"theme": "green", "color": "#44b78b", "title": "Green"},
    {"theme": "light-green", "color": "#2faa60", "title": "Light Green"},
    {"theme": "light-violet", "color": "#a464c4", "title": "Light Violet"},
    {"theme": "light-blue", "color": "#5EADDE", "title": "Light Blue"},
    {"theme": "light-gray", "color": "#222", "title": "Light Gray"},
]

JET_INDEX_DASHBOARD = "jet.dashboard.dashboard.DefaultIndexDashboard"
JET_APP_INDEX_DASHBOARD = "jet.dashboard.dashboard.DefaultAppIndexDashboard"
DDPAUTH_FORGOTTEN_PASSWORD_TOKEN_LENGTH = 20
DDPAUTH_FORGOTTEN_PASSWORD_TOKEN_VALIDITY_SECONDS = 10 * 60
DDPAUTH_FORGOTTEN_PASSWORD_SERIES_LENGTH = 20

DDP_DEVICE_USE_EVENT_MIN_SPEED_KPH = 5
DDP_MOBILE_EVENT_MIN_SPEED_KPH = 7