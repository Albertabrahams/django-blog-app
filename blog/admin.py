from django.contrib import admin
from .models import Like, Post, Category, Comments

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comments)
admin.site.register(Category)
