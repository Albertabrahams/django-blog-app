from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50)

    def _str_(self):
        return self.name
class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="media/", blank=True, default='media/noimage.webp')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

