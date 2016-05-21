from django.shortcuts import render
from django.shortcuts import redirect
from yg_cms.models import Column
from yg_cms.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    articles = Article.objects.all()[:6]
    columns = Column.objects.all()
    context = {'columns': columns, 'articles': articles}
    return render(request, 'index.html', context) #context_instance=RequestContext(request))


def column_detail(request, column_slug):
    columns = Column.objects.all()
    column = Column.objects.get(slug=column_slug)
    article_list = column.article_set.all()
    paginator = Paginator(article_list, 2) #实例化分页对象
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    context = {'column': column, 'columns': columns, 'article_list': article_list}
    return render(request, 'terms.html', context)


def article_detail(request, pk, article_slug):
    columns = Column.objects.all()
    articles = Article.objects.get(pk=pk)
    context = {'articles': articles, 'columns': columns}
    return render(request, 'single.html', context)


def archive(request, archive_slug):
    archives = Article.objects.filter(pub_date__month=archive_slug)
    context = {'archives': archives}
    return render(request, 'archive.html', context)


def me(request):
    return render('request', 'me.html',)
