from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    cover_img = models.ImageField( upload_to= 'post_img/' )
    title = models.CharField( max_length = 512 )
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey( User, on_delete = models.CASCADE )
    date_posted = models.DateTimeField(auto_now_add = True )
    is_posted = models.BooleanField( default = False)


