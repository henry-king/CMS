from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField(verbose_name='栏目名称', max_length=256)
    slug = models.CharField(verbose_name='栏目网址', max_length=256, db_index=True)
    intro = models.TextField(verbose_name='栏目介绍',default='')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']

@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
    title = models.CharField(verbose_name='标题')
    slug = models.CharField(  会尽快发多少就好好呵呵verbose_name='网址', max_length=256, db_index=True)
    author = models.ForeignKey('auth.User',blank=True, null=True, verbowe_name='作者')
    published = models.BooleanField(verbose_name='正式发布', default=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='教程'
        verbose_name_plural='教程'