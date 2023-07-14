from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey("DrinksCategory", default=None, on_delete=models.PROTECT)
    
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)
    
class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    