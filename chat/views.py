from django.shortcuts import render
from chat.models import Message


# Create your views here.
def home(request):
    if request.method == 'POST':
        message = request.POST['message']

        if message is not '':
            Message.objects.create(body=message)

    messages = Message.objects.all()
    return render(request, 'home.html', {'messages': messages})
