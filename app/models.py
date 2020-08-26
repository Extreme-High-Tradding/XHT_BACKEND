from django.db import models
from django.utils import timezone

# Testing room models

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    user = models.TextField(null=True,blank=True)
    amount = models.TextField(null=True,blank=True)
    price = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

# XHT models

class Money(models.Model):
    actual_money = models.DecimalField(max_digits=19, decimal_places=10)
    active1_average_price_date = models.DecimalField(max_digits=19, decimal_places=10)
    active2_average_price_date = models.DecimalField(max_digits=19, decimal_places=10)
    active3_average_price_date = models.DecimalField(max_digits=19, decimal_places=10)
    

class Users(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Transacctions(models.Model):
    
    buy_price_opened = models.DecimalField(max_digits=19, decimal_places=10)
    sell_price_closed = models.DecimalField(max_digits=19, decimal_places=10)
    amount_actives = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    active_id = models.CharField(max_length=50)