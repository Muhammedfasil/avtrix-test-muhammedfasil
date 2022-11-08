from unicodedata import category
from django.db import models
from datetime import datetime

# Create your models here.

class Foods(models.Model):
    order_date = models.DateTimeField(default=datetime.now)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return self.product