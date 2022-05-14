from django.urls import path
from . import views

app_name='summermodel'
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:article_id',views.detail,name='detail'),

]