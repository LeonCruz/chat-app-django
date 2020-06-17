from django.shortcuts import render, redirect, Http404
from chat.models import Message
from django.utils import timezone
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['login']
        user = authenticate(username=username)

        if user is not None:
            login(request, user)
            return redirect('/chat/')
        else:
            Http404()
            
    return render(request, 'home.html')


def add_message(request):
    message = request.POST['message']

    if message != '':
        Message.objects.create(body=message, time=timezone.now())

    return redirect('chat')


def chat(request):
    messages = Message.objects.all()
    return render(request, 'chat.html', {'messages': messages})
