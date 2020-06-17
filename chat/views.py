from django.shortcuts import render, redirect, Http404
from chat.models import Message
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['login']

        if username == '':
            error = 'O login não pode ser vazio'
            return render(request, 'home.html', {'error': error})

        try:
            user = User.objects.create(username=username)
        except IntegrityError:
            error = 'O login já está em uso'
            return render(request, 'home.html', {'error': error})
       
        user_auth = authenticate(username=username)

        if user_auth is not None:
            login(request, user_auth)
            return redirect('/chat/')
            
    return render(request, 'home.html')


def add_message(request):
    message = request.POST['message']

    if message != '':
        Message.objects.create(body=message, time=timezone.now())

    return redirect('/chat/')


def chat(request):
    messages = Message.objects.all()
    return render(request, 'chat.html', {'messages': messages})
