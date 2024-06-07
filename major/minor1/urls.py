from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_index,name="all index"),
    path('<int:car_id>', views.car_details,name="car_detail"),
    path('car_stores/', views.car_stores,name="car_stores"),
]
