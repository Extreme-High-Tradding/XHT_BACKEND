from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('transactions', views.transactions, name='transactions'), 
]
