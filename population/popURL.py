import django
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, "shlink")
SETTINGS = os.path.join(PROJECT_DIR, "settings.py")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shlink.settings")

django.setup()

from main import models

if __name__ == '__main__':
    for i in range(10):
        url = models.ShortenedURL(name=str(i), url="https://google.com")
        url.save()
