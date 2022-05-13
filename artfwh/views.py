from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def articleTop(request):
     return render(request,'artfwh/top.html')

def AboutBase(request):
     return render(request, 'artfwh/article_About.html')

def articlesDetail(request):
     return render(request,'artfwh/article_Main.html')
