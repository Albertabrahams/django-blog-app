from django.urls import path
from .views import post_list, post_create, post_update, post_delete, post_detail

urlpatterns = [
    path('',post_list , name='home'),
    path('create/',post_create , name='create'),
    path('update/<int:id>',post_update , name='update'),
    path('delete/<int:id>',post_delete , name='delete'),
    path('detail/<int:id>', post_detail, name="detail"),
    path('like/<int:id>', post_detail, name="like")
]