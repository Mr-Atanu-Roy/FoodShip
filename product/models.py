from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from string import digits
from unicodedata import decimal
from django.db import models
import uuid

from restaurant.models import *

food_type_choices = (
        ('veg', 'veg'),
        ('non-veg', 'non veg'),
    )

meal_type_choices = (
        ('starter', 'starter'),
        ('desert', 'desert'),
        ('snaks', 'snaks'),
        ('meal', 'meal'),
        ('drinks', 'drinks'),
        ('street-food', 'street-food'),
        ('biryani', 'biryani'),
        ('salad', 'salad'),
    )


# Create your models here.
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, unique=True, default = uuid.uuid4, editable=False)
    product_name = models.CharField(max_length = 255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_image = models.FileField(upload_to = 'product/', max_length=555)
    food_type = models.CharField(max_length=255, choices = food_type_choices, default='veg')
    meal_type = models.CharField(max_length=255, choices = meal_type_choices, default='starter')
    added_on = models.DateField(auto_now = True)

    @property
    def get_restaurantID(self):
        return self.restaurant.restaurant_id

    @property
    def get_restaurantName(self):
        return self.restaurant.restaurant_name

    def __str__(self):
        return self.product_name