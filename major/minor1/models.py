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
    cars = models.ForeignKey(CarVariety, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default= timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.cars.name}'

# Many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    car_varieties = models.ManyToManyField(CarVariety, related_name='stores')
    
    def __str__(self):
        return self.name
    
#one to one 
class CarCertificate(models.Model):
    cars = models.OneToOneField(CarVariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for{self.name.cars}'
    