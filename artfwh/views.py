from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *


# Create your views here.
def articleTop(request):
    about = AboutM.objects.order_by('-id')
    return render(request, 'artfwh/top.html',{'about':about})


def AboutBase(request,about_id):
    params={
        'Abou': AboutM.objects.order_by('-id'),
        'about': get_object_or_404(AboutM, id=about_id)
    }
    return render(request, 'artfwh/article_About.html', params)

def AboutBase2(request,number):
    params={
        'Abou': AboutM.objects.order_by('-id'),
        'about2': get_object_or_404(AboutM, id=number)
    }
    return render(request, 'artfwh/article_About2.html', params)


def artMain(request, art_id):
    art = get_object_or_404(ArticleM, id=art_id)
    return render(request, 'artfwh/article_Main.html', {'article': art})
