from channels import Group
from channels.sessions import channel_session
from .models import Room
import json
import re


@channel_session
def ws_connect(message):
    prefix= 'testroom'
    label = 'testroom'
    room = Room.objects.get(label='testroom')
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = 'testroom'

@channel_session
def ws_receive(message):
    label = 'testroom'
    room = Room.objects.get(label='testroom')
    data = json.loads(message['text'])
    m = room.messages.create(handle=data['handle'], message=data['message'], user=data['user'], amount=data['amount'],price=data['price'])
    Group('chat-'+label).send({'text': json.dumps(m.content)})

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)