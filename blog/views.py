from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
# Create your views here.
def list(request):

    #sacar articulos
    articles = Article.objects.all()

    #Paginar articulos
    paginator = Paginator(articles, 1)

    #recoger numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)


    return render(request, 'articles/list.html',{
        'title' :'Articulos',
        'articulos' : page_articles,
        'papamono': 'papamono'
    })



def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articulos = Article.objects.filter(categories=category_id)

    return render(request, 'categories/category.html', {
        'category': category,
        'articulos': articulos
    })

def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render (request, 'articles/detail.html', {
        'article' : article
    })
