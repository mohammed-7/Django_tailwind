from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_index,name="all index"),
    path('order/', views.order,name="order"),
]
