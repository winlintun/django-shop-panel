from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, help_text='Customer Name')
    email = models.EmailField(help_text="Email")
    phone = models.CharField(max_length=100, help_text='Phone Number: 09-255458532')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

