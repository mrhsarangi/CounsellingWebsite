from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    

    class Role(models.TextChoices):


        STUDENT = 'STUDENT', 'student'
        COUNSELOR = 'COUNSELOR', 'counselor'
        ADMIN = 'ADMIN', 'admin'

    username = models.CharField( max_length = 35, unique = True )
    user_type = models.CharField( max_length = 9, choices = Role.choices, default = Role.STUDENT )
    email = models.EmailField( max_length = 50, unique = True )
    slug = models.SlugField( unique = True, null = False )

    REQUIRED_FIELDS = ( 'user_type', 'email' )

    def __str__(self) -> str:
        return self.username.title()