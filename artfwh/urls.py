from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'artfwh'
urlpatterns = [
    path('', views.articleTop, name='artTop'),
    path('about/', views.AboutBase, name='about'),
    path('main/', views.articlesDetail, name='main'),

]
