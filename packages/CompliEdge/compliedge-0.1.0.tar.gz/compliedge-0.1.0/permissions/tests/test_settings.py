# Test settings for permissions app
import os
from compliedge.settings import *

# Use in-memory database for tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Use a separate secret key for tests
SECRET_KEY = 'test-secret-key-for-testing-purposes-only'

# Disable migrations for faster tests
class DisableMigrations:
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Use console email backend for tests
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Test media root
MEDIA_ROOT = os.path.join(BASE_DIR, 'test_media')

# Test static root
STATIC_ROOT = os.path.join(BASE_DIR, 'test_static')