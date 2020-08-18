# Generated by Django 3.0.8 on 2020-07-08 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='本文')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Blog', verbose_name='どの記事へのコメントか')),
            ],
        ),
    ]