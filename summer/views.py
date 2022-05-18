from django.shortcuts import render,get_object_or_404
from .models import ArticleM

# Create your views here.
# def index(request):
#     article=ArticleM.objects.order_by('-id')
#     return render(request,'summer/index.html',{'article':article})
#
# def detail(request,article_id):
#     article_text=get_object_or_404(ArticleM,id=article_id)
#     return render(request,'summer/detail.html',{'article_text':article_text})
