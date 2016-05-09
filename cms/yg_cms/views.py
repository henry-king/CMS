from django.shortcuts import render
from django.shortcuts import redirect
from yg_cms.models import Column
from yg_cms.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.template import RequestContext


def index(request):
    articles = Article.objects.all()
    columns = Column.objects.all()
    context = {'columns': columns, 'articles': articles}
    return render(request, 'index.html', context) #context_instance=RequestContext(request))


def column_detail(request, column_slug):
    columns = Column.objects.all()
    column = Column.objects.get(slug=column_slug)
    article_list = column.article_set.all()
    paginator = Paginator(article_list, 3) #实例化分页对象
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {'column': column, 'columns': columns, 'articles': articles}
    return render(request, 'news/column.html', context)


def article_detail(request, pk, article_slug):
    columns = Column.objects.all()
    articles = Article.objects.get(pk=pk)
    context = {'articles': articles, 'columns': columns}
    #if article_slug != article.slug:
        #return redirect(article,permanent=True)

    return render(request, 'news/article.html', context)
