from django.shortcuts import render
from .models import CarVariety

# Create your views here.

def all_index(request):
    cars = CarVariety.objects.all()    
    return render(request,'app/all_index.html',{'cars':cars})

def order(request):
    return render(request,'app/order.html')