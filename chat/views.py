from django.shortcuts import render, redirect
from chat.models import Message
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'home.html')


def add_message(request):
    message = request.POST['message']

    if message is not '':
        Message.objects.create(body=message, time=timezone.now())

    return redirect('chat')


def chat(request):
    messages = Message.objects.all()
    return render(request, 'messages.html', {'messages': messages})
