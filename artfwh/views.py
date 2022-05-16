from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from summer.models import ArticleM


# Create your views here.
def articleTop(request):
    return render(request, 'artfwh/top.html')


def AboutBase(request):
    articles = ArticleM.objects.order_by('-id')
    return render(request, 'artfwh/article_About.html', {'articles': articles})


def artMain(request, art_id):
    art = get_object_or_404(ArticleM, id=art_id)
    return render(request, 'artfwh/article_Main.html', {'article': art})
