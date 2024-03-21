# Generated by Django 5.0.3 on 2024-03-19 11:32

import posts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_author_alter_post_cover_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/', validators=[posts.models.Post.validate_image]),
        ),
    ]
