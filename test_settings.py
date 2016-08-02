SECRET_KEY = 'test'

DEBUG = True

ALLOWED_HOSTS = '*'

ROOT_URLCONF = 'financial_transactions.urls'

DEBUG_TOOLBAR_PATCH_SETTINGS = False

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/test_financial_transactions.db',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'categories',
    'django.contrib.contenttypes',
    'financial_transactions',
]

"""
To set SITE_ID:

Open: python manage.py shell

there:

from django.contrib.sites.models import Site
new_site = Site.objects.create(domain='127.0.0.1', name='127.0.0.1')
print new_site.id
"""
SITE_ID = 2

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

APPEND_SLASH = True

SOUTH_DATABASE_ADAPTERS = {}

# Support different currency formats.
USE_L10N = True
