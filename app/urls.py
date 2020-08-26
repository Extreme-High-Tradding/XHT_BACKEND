from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('chat', views.chat_room, name='chat_room'), 
]
