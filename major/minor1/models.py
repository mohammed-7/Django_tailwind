from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class CarVariety(models.Model):
    CAR_TYPE_CHOICE = [
        ('HB','Hatch back'),
        ('Lx','luxury'),
        ('Cp','Coupe'),
        ('Ul','Ultra luxury'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'minor1/')
    date_added = models.DateField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CAR_TYPE_CHOICE,default='Lx')
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
# one to many 
class CarReview(models.Model):
    cars = models.ForeignKey(CarVariety, on_delete=models.CASCADE)