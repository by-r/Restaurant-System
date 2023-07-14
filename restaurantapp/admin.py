from django.contrib import admin
from restaurantapp.models import Drinks, DrinksCategory, Reservation

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Reservation)