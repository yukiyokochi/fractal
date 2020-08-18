# Generated by Django 3.0.8 on 2020-07-09 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_blog_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='blog.Blog', verbose_name='対象記事'),
        ),
    ]