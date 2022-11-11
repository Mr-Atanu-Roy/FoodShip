from django.db import models

from django.utils import timezone
import uuid

from auditlog.registry import auditlog

restaurant_type_choices = (
        ('family', 'family'),
        ('pub', 'pub'),
        ('fast-food', 'fast-food'),
        ('dinner', 'dinner'),
        ('cafe', 'cafe'),
    )

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    restaurant_name = models.CharField(max_length = 255)
    restaurant_image = models.FileField(upload_to= 'restaurant/', max_length=555, default=None)
    restaurant_type = models.CharField(max_length=255, choices = restaurant_type_choices, default='family')
    available_foodTypes = models.CharField(max_length = 255, blank = True)
    country = models.CharField(max_length = 255, blank = True)
    state = models.CharField(max_length = 255, blank = True)
    city = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    pin = models.IntegerField()
    phone = models.IntegerField()
    timing = models.CharField(max_length = 255, default = "10 AM to 12 Midnight")
    rating = models.DecimalField(max_digits = 2, decimal_places=1)

    #facilities
    home_delivery = models.BooleanField(default = False)
    full_bar_available = models.BooleanField(default = False)
    takeaway_available = models.BooleanField(default = False)
    vegitarian_only = models.BooleanField(default = False)
    live_sports_screening = models.BooleanField(default = False)
    deserts_and_bakes = models.BooleanField(default = False)
    live_music = models.BooleanField(default = False)
    smoking_area = models.BooleanField(default = False)
    family_dining = models.BooleanField(default = False)
    romantic_dining = models.BooleanField(default = False)
    indoor_seating = models.BooleanField(default = False)
    outdoor_seating = models.BooleanField(default = False)
    nightlife = models.BooleanField(default = False)
    free_wifi = models.BooleanField(default = False)
    pool = models.BooleanField(default = False)

    def __str__(self):
        return self.restaurant_name


class RestaurantReview(models.Model):
    review_id = models.UUIDField(primary_key=True, unique=True, default = uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.DecimalField(max_digits = 2, decimal_places=1)
    added_on = models.DateField(default=timezone.now)

auditlog.register(Restaurant)  
auditlog.register(RestaurantReview) 