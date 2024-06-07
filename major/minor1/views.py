from django.shortcuts import render
from .models import CarVariety,Store
from django.shortcuts import get_object_or_404
from .forms import CarVarietyForm
# Create your views here.

def all_index(request):
    cars = CarVariety.objects.all()    
    return render(request,'app/all_index.html',{'cars':cars})

def car_details(request,car_id):
    cars = get_object_or_404(CarVariety,pk=car_id)
    return render(request,'app/car_details.html',{'cars':cars})

def car_stores(request):
    stores = None 
    if request.method == 'POST':
        form = CarVarietyForm(request.POST)
        if form.is_valid():
            car_variety = form.cleaned_data['car_variety']
            Store.objects.filter(car_varieties = car_variety)
    else:
        form = CarVarietyForm()
    return render(request,'app/car_stores.html',{'stores':stores , 'form':form})