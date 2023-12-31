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
        'DIRS': [],
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
STATIC_ROOT = path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ["127.0.0.1"]

# JAZZMIN_SETTINGS = {
#     # title of the window (Will default to current_admin_site.site_title if absent or None)
#     "site_title": "Admin Panel",
#
#     # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
#     "site_header": "Admin Panel",
#
#     # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
#     "site_brand": "DoodMall",
#
#     # Logo to use for your site, must be present in static files, used for brand on top left
#     # "site_logo": "books/img/logo.png",
#
#     # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
#     "login_logo": None,
#
#     # Logo to use for login form in dark themes (defaults to login_logo)
#     "login_logo_dark": None,
#
#     # CSS classes that are applied to the logo above
#     "site_logo_classes": "img-circle",
#
#     # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
#     "site_icon": None,
#
#     # Welcome text on the login screen
#     "welcome_sign": "Welcome to the Admin Panel",
#
#     # Copyright on the footer
#     "copyright": "OOO DoodMall Team",
#
#     # List of model admins to search from the search bar, search bar omitted if excluded
#     # If you want to use a single search field you don't need to use a list, you can use a simple string
#     "search_model": ["auth.User", "auth.Group"],
#
#     # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
#     "user_avatar": None,
#
#     ############
#     # Top Menu #
#     ############
#
#     # Links to put along the top menu
#     "topmenu_links": [
#
#         # Url that gets reversed (Permissions can be added)
#         {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
#
#         # external url that opens in a new window (Permissions can be added)
#         {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
#
#         # model admin to link to (Permissions checked against model)
#         {"model": "auth.User"},
#
#         # App with dropdown menu to all its models pages (Permissions checked against models)
#         {"app": "users", "groups": ["auth.Group"]},
#     ],
#
#     #############
#     # User Menu #
#     #############
#
#     # Additional links to include in the user menu on the top right ("app" url type is not allowed)
#     "usermenu_links": [
#         {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
#         {"model": "auth.user"}
#     ],
#
#     #############
#     # Side Menu #
#     #############
#
#     # Whether to display the side menu
#     "show_sidebar": True,
#
#     # Whether to aut expand the menu
#     "navigation_expanded": True,
#
#     # Hide these apps when generating side menu e.g (auth)
#     "hide_apps": [],
#
#     # Hide these models when generating side menu (e.g auth.user)
#     "hide_models": [],
#
#     # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
#     "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
#
#     # Custom links to append to app groups, keyed on app name
#     "custom_links": {
#         "books": [{
#             "name": "Make Messages",
#             "url": "make_messages",
#             "icon": "fas fa-comments",
#             "permissions": ["books.view_book"]
#         }]
#     },
#
#     # for the full list of 5.13.0 free icon classes
#     "icons": {
#         "auth": "fas fa-users-cog",
#         "auth.user": "fas fa-user",
#         "auth.Group": "fas fa-users",
#     },
#     # Icons that are used when one is not manually specified
#     "default_icon_parents": "fas fa-chevron-circle-right",
#     "default_icon_children": "fas fa-circle",
#
#     #################
#     # Related Modal #
#     #################
#     # Use modals instead of popups
#     "related_modal_active": False,
#
#     #############
#     # UI Tweaks #
#     #############
#     # Relative paths to custom CSS/JS scripts (must be present in static files)
#     "custom_css": None,
#     "custom_js": None,
#     # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
#     "use_google_fonts_cdn": True,
#     # Whether to show the UI customizer on the sidebar
#     "show_ui_builder": False,
#
#     ###############
#     # Change view #
#     ###############
#     # Render out the change view as a single form, or in tabs, current options are
#     # - single
#     # - horizontal_tabs (default)
#     # - vertical_tabs
#     # - collapsible
#     # - carousel
#     "changeform_format": "horizontal_tabs",
#     # override change forms on a per modeladmin basis
#     "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
#     # Add a language dropdown into the admin
#     # "language_chooser": True,
# }

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

JAZZMIN_SETTINGS = {
    "site_brand": "DoodMall",
    "copyright": "OOO DoodMall Team",

    'show_ui_builder': True
}
