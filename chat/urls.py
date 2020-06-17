from django.urls import path
from chat import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_message', views.add_message, name='add_message'),
    path('chat/', views.chat, name='chat'),
]
