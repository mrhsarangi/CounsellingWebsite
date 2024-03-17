from django.urls import path
from .views import CreatePost, UpdatePost, DeletePost

app_name = 'posts'
urlpatterns = [
    path('create-post/', CreatePost.as_view(), name='create'),
    path('<slug:slug>/update-post/', UpdatePost.as_view(), name='update'),
    path('<slug:slug>/delete-post/', DeletePost.as_view(), name='delete'),


]