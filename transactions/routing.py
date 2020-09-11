from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/buy/$', consumers.BuyConsumer),
    re_path(r'ws/opensell/$', consumers.OpendSellConsumer),
    re_path(r'ws/closesell/$', consumers.CloseSellConsumer),
]