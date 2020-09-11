from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/balance/$', consumers.BalanceConsumer),
    re_path(r'ws/assets/$', consumers.AssetsConsumer),
]