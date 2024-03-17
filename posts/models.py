from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    cover_img = models.ImageField( upload_to= 'post_img/', null=True, blank= True )
    title = models.CharField( max_length = 512 )
    content = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey( get_user_model(), on_delete = models.CASCADE )
    date_posted = models.DateTimeField(auto_now_add = True )
    is_posted = models.BooleanField( default = False)


