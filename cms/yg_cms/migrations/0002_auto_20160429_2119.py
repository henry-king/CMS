# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 13:19
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yg_cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=256, unique=True, verbose_name='网址'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='标题a'),
        ),
    ]
