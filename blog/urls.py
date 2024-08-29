from django.urls import path
from .views import post_detail, render_posts

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail')
]