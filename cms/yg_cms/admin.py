from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article
from .models import Column


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro',)


class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')


admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
