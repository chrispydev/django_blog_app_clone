from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media_file', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
