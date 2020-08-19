from django.urls import re_path
from operations import consumer

websocket_urlpatterns = [
    re_path(r'ws/operations/(?P<room_name>\w+)/$', consumer.OperationsConsumer),
]
