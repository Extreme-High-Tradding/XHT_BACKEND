from django.urls import path
from . import views as operations_views

urlpatterns = [
    path('', operations_views.index, name='index'),
     path('<str:room_name>/', operations_views.room, name='room'),
]