# Generated by Django 5.0.3 on 2024-03-19 11:32

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='profile_pics', validators=[accounts.models.User.validate_image]),
        ),
    ]