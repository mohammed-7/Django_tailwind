from django.shortcuts import render
# Create your views here.
def all_index(request):
    
    return render(request,'app/all_index.html',{'cars':cars})

def order(request):
    return render(request,'app/order.html')