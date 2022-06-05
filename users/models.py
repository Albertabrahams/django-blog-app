import email
from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username.username