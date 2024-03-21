from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Create your models here.
class Post(models.Model):

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    cover_img = models.ImageField( upload_to= 'post_img/', null=True, blank= True, validators=[ validate_image] )
    title = models.CharField( max_length = 512 )
    content = models.TextField()
    slug = models.SlugField(unique = True)
    author = models.ForeignKey( get_user_model(), on_delete = models.CASCADE, related_name = 'posts')
    date_posted = models.DateTimeField(auto_now_add = True )
    save_as_draft = models.BooleanField( default = False)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    comment = models.CharField(max_length = 512)


class Reply(models.Model):

    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = 'reply')
    reply = models.CharField(max_length = 512)
