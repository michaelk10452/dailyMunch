from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    yelp_id = models.CharField(max_length=30)
    data = models.JSONField()
    def __str__(self):
        return f'{self.data["name"]}'

class Visited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_visited = models.DateField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    distance_miles = models.DecimalField(max_digits=3, decimal_places=1, default=10.0)
    price = models.CharField(max_length=1, default='3')
    open_now = models.BooleanField(default=True)
    trendy = models.BooleanField(default=False)
    reservation = models.BooleanField(default=False)
    pickup = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)






