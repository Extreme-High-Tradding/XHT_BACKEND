from django.db import models
from django.utils import timezone

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

class Test(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)