"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")
django.setup()

from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
import api.routing
application = ProtocolTypeRouter(
    {"http": get_asgi_application(), "websocket": URLRouter(api.routing.websocket_urls)}
)
