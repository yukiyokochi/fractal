from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.



class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category,verbose_name='カテゴリ',on_delete=models.PROTECT,related_name='blogs')
    writer = models.CharField('投稿者',max_length=255,default="名無しさん")
    title = models.CharField('記事タイトル',max_length=255)
    text = models.TextField('記事本文',blank=False)
    created_at = models.DateTimeField('作成日',default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    # like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.CharField('ニックネーム',max_length=255,default="名無しさん")
    text = models.TextField('コメント')
    target = models.ForeignKey(Blog,on_delete=models.PROTECT, verbose_name="対象記事")
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.text[:999]
