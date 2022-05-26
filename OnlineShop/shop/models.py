from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, help_text='Customer Name: Win Lin Tun')
    email = models.EmailField(help_text="Email: netuser979@gmail.com")
    phone = models.CharField(max_length=100, help_text='Phone Number: 09-255458532')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = (
        ('indoor', 'In Door'),
        ('outdoor', "Out Door")
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=category)
    description = models.TextField(help_text="Detail Product", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.name