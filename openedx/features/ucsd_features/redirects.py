from django.conf import settings
from django.conf.urls import url
from django.shortcuts import redirect

from logging import getLogger

# Import the URL configuration module for the current environment
import importlib
urls = importlib.import_module(settings.ROOT_URLCONF)

log = getLogger(__name__)


def callback_generator(destination):
    def callback(request):
        return redirect(destination)
    return callback

patterns = []
if hasattr(settings, "ENV_TOKENS"):
    patterns = settings.ENV_TOKENS.get("UCSD_REDIRECT_URLS", [])

# Iterate in reverse order, so that the first redirect listeed ends up in the first element of the URL Patterns array
for pattern in patterns[::-1]:
    log.info("Redirecting route {} to {}".format(pattern['route'], pattern['dest']))

    # A request is handled by the first matching route, so these overrides must be prepended
    urls.urlpatterns.insert(0, url(pattern['route'], callback_generator(pattern['dest'])))
