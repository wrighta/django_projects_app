from django.shortcuts import render
from .models import Message

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'messages/message_list.html', {'messages': messages})


def messages(request):
    return render(request, 'messages/messages.html')
