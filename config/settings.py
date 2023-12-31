from os import path, getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    # Admin Panel
    'jazzmin',
    # Django Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom Apps
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    # Third Party Apps
    'drf_yasg',
    'debug_toolbar',
    'parler',
    'django_filters',
]

MIDDLEWARE = [
    # Default
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Other
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PSWD'),
        'HOST': getenv('DB_HOST'),
        'PORT': getenv('DB_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.users.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.users.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.users.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.users.password_validation.NumericPasswordValidator'}
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
# STATIC_ROOT = path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    path.join(BASE_DIR, 'static')
]
MEDIA_URL = 'media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ["127.0.0.1"]

# Parler's settings section

PARLER_DEFAULT_LANGUAGE_CODE = 'en'
PARLER_ENABLE_CACHING = True
PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'uz'},
        {'code': 'ru'},
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False
    }
}

# Jazzmin settings section

JAZZMIN_SETTINGS = {
    "site_brand": "DoodMall",
    "site_logo": "/main/img/logo.png",
    "copyright": "OOO DoodMall Team",

    'show_ui_builder': True
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True,
}

