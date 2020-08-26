from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

class Test(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)