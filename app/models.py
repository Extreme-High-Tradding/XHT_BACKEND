from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

class Financial(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    balance = models.DecimalField(default = 100000.000000, max_digits=19, decimal_places=6 )
    active1_average_price = models.DecimalField(default = 0, blank = True, max_digits=19, decimal_places=10)
    active2_average_price = models.DecimalField(default = 0, blank = True, max_digits=19, decimal_places=10)
    active3_average_price = models.DecimalField(default = 0, blank = True, max_digits=19, decimal_places=10)
    active1_amount = models.DecimalField(default = 0, blank = True, max_digits=19, decimal_places=10)
    active2_amount = models.DecimalField(default = 0, blank = True, max_digits=19, decimal_places=10)
    active3_amount = models.DecimalField(default = 0, blank = True, max_digits=19, decimal_places=10)


class Transacctions(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    opening_price = models.DecimalField(max_digits=19, decimal_places=6)
    closing_price = models.DecimalField(default = 0, blank = True, null = True, max_digits=19, decimal_places=6)
    amount_assets = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)
    asset_id = models.CharField(max_length = 50)# asset_id = 'tesla', 'petroleo', 'bitcoin'
    operation_type = models.BooleanField(default = False)# False= = 'Buy', True = 'Sell' 
    operation_status = models.BooleanField(default = False)# False = open , False = 'close'