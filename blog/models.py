from django.db import models
from django.utils import timezone
from users.models import CustomUser

from django.urls import reverse
# Create your models here.
class Post(models.Model):
    text=models.CharField(max_length=300,default='')
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(default=timezone.now) 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
