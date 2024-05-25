from django.shortcuts import render
from .models import CarVariety
from django.shortcuts import get_object_or_404
# Create your views here.

def all_index(request):
    cars = CarVariety.objects.all()    
    return render(request,'app/all_index.html',{'cars':cars})

def car_details(request,car_id):
    cars = get_object_or_404(CarVariety,pk=car_id)
    return render(request,'app/car_details.html',{'cars':cars})