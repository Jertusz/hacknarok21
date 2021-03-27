from django.urls import re_path
from api import consumers

# localhost/ws/sessions/sdajlhsdahjsdajhsdajl/
websocket_urls = [
    re_path(r"ws/sessions/(?P<session_id>\w+)/$", consumers.SessionConsumer.as_asgi())
]
