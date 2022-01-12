from django.contrib import admin
from dailyMunch.models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('yelp_id', '__str__', 'data')

class VisitedAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'date_visited')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Visited, VisitedAdmin)
admin.site.register(Profile, ProfileAdmin)

