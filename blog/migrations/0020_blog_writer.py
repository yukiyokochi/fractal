# Generated by Django 3.0.8 on 2020-07-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_category_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(default='名無しさん', max_length=255, verbose_name='投稿者'),
        ),
    ]
