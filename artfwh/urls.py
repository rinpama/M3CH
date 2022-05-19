from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'artfwh'
urlpatterns = [
    path('', views.articleTop, name='artTop'),
    path('about/<int:about_id>', views.AboutBase, name='about'),
    path('about2/<int:number>', views.AboutBase2, name='about2'),
    path('main/<int:art_id>', views.artMain, name='main'),

]
