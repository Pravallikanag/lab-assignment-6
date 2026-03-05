from django.shortcuts import render
from .models import Message

# homepage
def home(request):
    return render(request, "home.html")

# dynamic greeting
def greet(request, name):
    return render(request, "greet.html", {"name": name})

# list messages
def message_list(request):
    messages = Message.objects.all()
    return render(request, "messages.html", {"messages": messages})
