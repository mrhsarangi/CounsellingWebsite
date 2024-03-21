from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    

    class Role(models.TextChoices):


        STUDENT = 'STUDENT', 'student'
        COUNSELOR = 'COUNSELOR', 'counselor'
        ADMIN = 'ADMIN', 'admin'

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    profile_img = models.ImageField(upload_to='profile_pics', null=True, validators=[validate_image], default='profile_pics/default_user.png')
    username = models.CharField( max_length = 35, unique = True )
    user_type = models.CharField( max_length = 9, choices = Role.choices, default = Role.STUDENT )
    email = models.EmailField( max_length = 50, unique = True )
    slug = models.SlugField( unique = True, null = False, default='' )

    REQUIRED_FIELDS = ( 'user_type', 'email' )

    def __str__(self) -> str:
        return self.username.title()
    