from django.db import models

# Create your models here.

address_type_choices = (
    ("home", "home"),
    ("office", "office"),
)

address_preference_choices = (
    ("primary", "primary"),
    ("secondary", "secondary"),
)

class UserProfile(models.Model):
    profile_id = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length = 255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

class UserAddress(models.Model):
    address_id = models.CharField(max_length=255, blank = True, null = True)
    email = models.CharField(max_length=255)
    address_email = models.CharField(max_length=255, blank = True, null = True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length = 255)
    landmark = models.CharField(max_length = 255, blank = True, null = True)
    pin = models.CharField(max_length = 255, blank = True, null = True)
    phone = models.CharField(max_length = 255, blank = True, null = True)
    address_preference = models.CharField(max_length = 255, choices = address_preference_choices, default = "secondary")
    address_type = models.CharField(max_length = 255, choices = address_type_choices)

    
    def __str__(self):
        return self.email+"/"+self.address_preference
    