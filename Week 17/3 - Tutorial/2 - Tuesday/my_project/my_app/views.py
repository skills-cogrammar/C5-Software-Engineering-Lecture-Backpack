from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users

sports = {"Rugby", "Cricker", "Tennis", "Soccer", "Hockey"}

# Create your views here.
def index(request):
    users = Users.objects.all().order_by("-date_registered")
    return render(request, 'index.html', {'users':users})

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html', {'sports': sports})

@csrf_exempt
def register_user(request):
    user = Users()
    user.username = request.POST['username']
    user.sport = request.POST['sport']
    user.save()
    return redirect('/my_app/')