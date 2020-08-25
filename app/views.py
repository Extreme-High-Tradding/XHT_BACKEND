def chat_room(request):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    
    room, created = Room.objects.get_or_create(label='testroom')

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
    })