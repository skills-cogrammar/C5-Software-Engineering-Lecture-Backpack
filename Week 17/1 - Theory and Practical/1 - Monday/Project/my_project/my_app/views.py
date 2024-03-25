from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.
def index(request):
    return render(request, 'main.html')

def welcome(request):
    name = request.GET.get("name")
    surname = request.GET.get("surname")
    user = User()
    user.name = name
    user.surname = surname
    user.save()
    return render(request, "welcome.html", {"name": name, "surname": surname})