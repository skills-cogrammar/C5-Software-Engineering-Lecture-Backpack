from django.shortcuts import render
from .models import Item

# Create your views here.
def view_products(request):
    items = Item.objects.all()
    return render(request, 'shop.html', {"items": items})