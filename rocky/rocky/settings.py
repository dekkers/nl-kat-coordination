"""
Django settings for rocky project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load variables from the .env file
load_dotenv(dotenv_path=BASE_DIR / ".env", verbose=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

QUEUE_NAME_BOEFJES = os.getenv("QUEUE_NAME_BOEFJES")
QUEUE_NAME_NORMALIZERS = os.getenv("QUEUE_NAME_NORMALIZERS")
QUEUE_URI = os.getenv("QUEUE_URI")

OCTOPOES_API = os.getenv("OCTOPOES_API")

SCHEDULER_API = os.getenv("SCHEDULER_API", "")

KATALOGUS_API = os.getenv("KATALOGUS_API", "")

BYTES_API = os.getenv("BYTES_API", "")
BYTES_USERNAME = os.getenv("BYTES_USERNAME", "")
BYTES_PASSWORD = os.getenv("BYTES_PASSWORD", "")

KEIKO_API = os.getenv("KEIKO_API", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == "True"
TWOFACTOR_ENABLED = os.getenv("TWOFACTOR_ENABLED") == "True"

ALLOWED_HOSTS = ["*"]

# -----------------------------
# EMAIL CONFIGURATION for SMTP
# -----------------------------
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_FILE_PATH = os.getenv("EMAIL_FILE_PATH", BASE_DIR / "rocky/email_logs")  # directory to store output files
EMAIL_HOST = os.getenv("EMAIL_HOST")  # localhost
EMAIL_PORT = os.getenv("EMAIL_PORT", 25)  # 25
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = os.getenv("SERVER_EMAIL")
EMAIL_SUBJECT_PREFIX = os.getenv("EMAIL_SUBJECT_PREFIX")  # "KAT - "
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", False)  # False
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", False)  # False
EMAIL_SSL_CERTFILE = os.getenv("EMAIL_SSL_CERTFILE", None)  # None
EMAIL_SSL_KEYFILE = os.getenv("EMAIL_SSL_KEYFILE", None)
EMAIL_TIMEOUT = 30  # 30 seconds
# ----------------------------

HELP_DESK_EMAIL = os.getenv("HELP_DESK_EMAIL", "")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "markdownify.apps.MarkdownifyConfig",
    "two_factor",
    "account",
    "tools",
    "fmea",
    "crisis_room",
    "onboarding",
    "katalogus",
    "django_password_validators",
    "django_password_validators.password_history",
    "rest_framework",
    "tagulous",
    # "drf_standardized_errors",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "rocky.middleware.onboarding.OnboardingMiddleware",
]

ROOT_URLCONF = "rocky.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "rocky/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "tools.context_processors.languages",
            ],
            "builtins": ["tools.templatetags.ooi_extra"],
        },
    },
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

WSGI_APPLICATION = "rocky.wsgi.application"

AUTH_USER_MODEL = "account.KATUser"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
POSTGRES_USER = os.getenv("ROCKY_DB_USER")
POSTGRES_PASSWORD = os.getenv("ROCKY_DB_PASSWORD")
POSTGRES_DB = os.getenv("ROCKY_DB")
POSTGRES_DB_HOST = os.getenv("ROCKY_DB_HOST")
POSTGRES_DB_PORT = os.getenv("ROCKY_DB_PORT")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_DB_HOST,
        "PORT": POSTGRES_DB_PORT,
    }
}

if os.getenv("POSTGRES_SSL_ENABLED"):
    DATABASES["default"]["OPTIONS"] = {
        "sslmode": os.getenv("POSTGRES_SSL_MODE"),
        "sslrootcert": os.getenv("POSTGRES_SSL_ROOTCERT"),
        "sslcert": os.getenv("POSTGRES_SSL_CERT"),
        "sslkey": os.getenv("POSTGRES_SSL_KEY"),
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": int(os.getenv("PASSWORD_MIN_LENGTH", 12)),
        },
    },
    {
        "NAME": "django_password_validators.password_character_requirements"
        ".password_validation.PasswordCharacterValidator",
        "OPTIONS": {
            "min_length_digit": int(os.getenv("PASSWORD_MIN_DIGIT", 2)),
            "min_length_alpha": int(os.getenv("PASSWORD_MIN_ALPHA", 2)),
            "min_length_special": int(os.getenv("PASSWORD_MIN_SPECIAL", 2)),
            "min_length_lower": int(os.getenv("PASSWORD_MIN_LOWER", 2)),
            "min_length_upper": int(os.getenv("PASSWORD_MIN_UPPER", 2)),
            "special_characters": " ~!@#$%^&*()_+{}\":;'[]",
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en"
LANGUAGE_COOKIE_NAME = "language"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (BASE_DIR / "rocky/locale",)

LANGUAGES = [
    ("en", "en"),
    ("nl", "nl"),
    ("pap", "pap"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "assets"),)

LOGIN_URL = "two_factor:login"
LOGIN_REDIRECT_URL = "crisis_room"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SESSION_EXPIRE_SECONDS = 60 * 60 * 2  # 2 hours
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

# Require session cookie to be secure, so only a https session can be started
SESSION_COOKIE_SECURE = True

# Also set the max age on the session cookie
SESSION_COOKIE_AGE = SESSION_EXPIRE_SECONDS

SESSION_COOKIE_SAMESITE = "Strict"

# only allow http to read session cookies, not Javascript
SESSION_COOKIE_HTTPONLY = True

# No secure connection means you're not allowed to submit a form
CSRF_COOKIE_SECURE = True

# Chrome does not send the csrfcookie
CSRF_COOKIE_SAMESITE = "Strict"

# only allow http to read csrf cookies, not Javascript
CSRF_COOKIE_HTTPONLY = True

# Setup sane security defaults for application
# Deny x-framing, which is standard since Django 3.0
# There is no need to embed this in a frame anywhere, not desired.
X_FRAME_OPTIONS = "DENY"
# Send some legacy security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

CSP_HEADER = os.getenv("CSP_HEADER", "True") == "True"

if CSP_HEADER:
    MIDDLEWARE += ["csp.middleware.CSPMiddleware"]
    INSTALLED_APPS += ["csp"]

CSP_DEFAULT_SRC = ["'none'"]
CSP_IMG_SRC = ["'self'"]
CSP_FONT_SRC = ["'self'"]
CSP_STYLE_SRC = ["'self'"]
CSP_FRAME_ANCESTORS = ["'none'"]
CSP_BASE = ["'none'"]
CSP_FORM_ACTION = ["'self'"]
CSP_INCLUDE_NONCE_IN = ["script-src"]

CSP_BLOCK_ALL_MIXED_CONTENT = True

# MarkDownify settings
# see https://django-markdownify.readthedocs.io/en/latest/settings.html
MARKDOWNIFY = {
    "default": {
        "WHITELIST_TAGS": [
            "a",
            "abbr",
            "acronym",
            "b",
            "br",
            "blockquote",
            "em",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "i",
            "li",
            "ol",
            "p",
            "pre",
            "strong",
            "table",
            "thead",
            "tbody",
            "th",
            "tr",
            "td",
            "ul",
        ],
        "MARKDOWN_EXTENSIONS": [
            "markdown.extensions.extra",
        ],
        "LINKIFY_TEXT": {
            "PARSE_URLS": False,
        },
    }
}

DEFAULT_RENDERER_CLASSES = ["rest_framework.renderers.JSONRenderer"]

# Turn on the browsable API by default if DEBUG is True, but disable by default in production
BROWSABLE_API = os.getenv("BROWSABLE_API", "True" if DEBUG else "False") == "True"

if BROWSABLE_API:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + ["rest_framework.renderers.BrowsableAPIRenderer"]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        # For now this will provide a safe default, but non-admin users will
        # need to be able to use the API in the future..
        "rest_framework.permissions.IsAdminUser",
    ],
    "DEFAULT_RENDERER_CLASSES": DEFAULT_RENDERER_CLASSES,
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}

SERIALIZATION_MODULES = {
    "xml": "tagulous.serializers.xml_serializer",
    "json": "tagulous.serializers.json",
    "python": "tagulous.serializers.python",
    "yaml": "tagulous.serializers.pyyaml",
}
TAGULOUS_SLUG_ALLOW_UNICODE = True

TAG_COLORS = [
    ("color-1-light", _("Blue light")),
    ("color-1-medium", _("Blue medium")),
    ("color-1-dark", _("Blue dark")),
    ("color-2-light", _("Green light")),
    ("color-2-medium", _("Green medium")),
    ("color-2-dark", _("Green dark")),
    ("color-3-light", _("Yellow light")),
    ("color-3-medium", _("Yellow medium")),
    ("color-3-dark", _("Yellow dark")),
    ("color-4-light", _("Orange light")),
    ("color-4-medium", _("Orange medium")),
    ("color-4-dark", _("Orange dark")),
    ("color-5-light", _("Red light")),
    ("color-5-medium", _("Red medium")),
    ("color-5-dark", _("Red dark")),
    ("color-6-light", _("Violet light")),
    ("color-6-medium", _("Violet medium")),
    ("color-6-dark", _("Violet dark")),
]

TAG_BORDER_TYPES = [
    ("plain", _("Plain")),
    ("solid", _("Solid")),
    ("dashed", _("Dashed")),
    ("dotted", _("Dotted")),
]
