from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=300,default='')
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(default=timezone.now)
    
