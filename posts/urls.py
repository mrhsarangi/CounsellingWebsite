from django.urls import path
from .views import CreatePost, UpdatePost, DeletePost, PostDetail

app_name = 'posts'
urlpatterns = [
    path('create/', CreatePost.as_view(), name='create'),
    path('<slug:slug>/update/', UpdatePost.as_view(), name='update'),
    path('<slug:slug>/delete/', DeletePost.as_view(), name='delete'),
    path('<slug:slug>/', PostDetail.as_view(), name='details'),


]