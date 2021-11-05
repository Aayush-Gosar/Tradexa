from django.db import models

from PIL import Image
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.BooleanField(default=False)
    last_name = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser , on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profilepics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    