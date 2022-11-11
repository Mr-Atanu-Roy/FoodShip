from django.db import models

from django.utils import timezone
import uuid
from auditlog.registry import auditlog

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
    added_on = models.DateTimeField(default=timezone.now)

    @property
    def get_restaurantID(self):
        return self.restaurant.restaurant_id

    @property
    def get_restaurantName(self):
        return self.restaurant.restaurant_name

    def __str__(self):
        return self.product_name


class ProductReview(models.Model):
    # review_id = models.UUIDField(primary_key=True, unique=True, default = uuid.uuid4, editable=False)
    product = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    review = models.TextField()
    rating = models.DecimalField(max_digits = 2, decimal_places=1)
    added_on = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.product}/{self.user}"


auditlog.register(Product)  
auditlog.register(ProductReview) 