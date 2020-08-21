import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
from .models import Room


def chat_room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "operations/room.html", {
        'room': room,
        'messages': messages,
    })