from django.db import models
from django.utils import timezone

# Create your models here.

order_status_choices = (
        ('ordered', 'ordered'),
        ('out for delivery', 'out for delivery'),
        ('delivered', 'delivered'),
        ('canceled', 'canceled'),
    )

class Order(models.Model):
    order_id = models.CharField(max_length = 255)
    payment_id = models.CharField(max_length = 255, blank = True)
    user = models.CharField(max_length = 255)
    buyer_name = models.CharField(max_length = 255, blank = True)
    phone = models.CharField(max_length = 255, blank = True, null = True)
    product = models.CharField(max_length = 255, blank = True)
    quantity = models.CharField(max_length = 255, blank = True)
    amount = models.CharField(max_length = 255, blank = True)
    payment_status = models.CharField(max_length = 255, default = "not done")
    payment_mode = models.CharField(max_length = 255, blank = True)
    order_status = models.CharField(max_length = 255, choices = order_status_choices, default = "canceled")
    address = models.CharField(max_length = 255, blank = True)
    payment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.order_id
