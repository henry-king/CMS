from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from yg_cms.models import Column
from yg_cms.models import Article


def index(request):
    articles = Article.objects.all()
    columns = Column.objects.all()
    context = {'columns': columns, 'articles': articles}
    return render(request, 'index.html', context)


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    context = {'column': column}
    return render(request, 'news/column.html', context)


def article_detail(request, pk,article_slug):
    articles = Article.objects.get(pk=pk)
    context = {'articles': articles}
    #if article_slug != article.slug:
        #return redirect(article,permanent=True)
    return render(request, 'news/article.html', context)
