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
    actual_money = models.DecimalField(blank = False, max_digits=19, decimal_places=6 )
    active1_average_price_date = models.DecimalField(blank = True, max_digits=19, decimal_places=10)
    active2_average_price_date = models.DecimalField(blank = True,max_digits=19, decimal_places=10)
    active3_average_price_date = models.DecimalField(blank = True,max_digits=19, decimal_places=10)
    active1_amount = models.DecimalField(blank = True, max_digits=19, decimal_places=10)
    active2_amount = models.DecimalField(blank = True, max_digits=19, decimal_places=10)
    active3_amount = models.DecimalField(blank = True, max_digits=19, decimal_places=10)


class Transacctions(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    price_opened = models.DecimalField(max_digits=19, decimal_places=6)
    price_closed = models.DecimalField(blank = True, null = True, max_digits=19, decimal_places=6)
    amount_actives = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    active_id = models.CharField(max_length=50)
    operation_type = models.BooleanField(default= False)
    operation_status = models.BooleanField()