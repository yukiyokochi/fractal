# Generated by Django 3.0.8 on 2020-07-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_blog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]