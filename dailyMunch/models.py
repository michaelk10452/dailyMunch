from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    yelp_id = models.CharField(max_length=30)
    data = models.JSONField()

class Visited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    distance_miles = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.CharField(max_length=1)
    trendy = models.BooleanField()
    reservation = models.BooleanField()
    pickup = models.BooleanField()
    delivery = models.BooleanField()



