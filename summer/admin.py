from django.contrib import admin
from .models import eraM,genreM,AboutM,mainWordM,ArticleM

from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class ArticleMAdmin(SummernoteModelAdmin):
    summernote_fields= '__all__'
class AboutMAdmin(SummernoteModelAdmin):
    summernote_fields= '__all__'

admin.site.register(ArticleM,ArticleMAdmin)
admin.site.register(AboutM,AboutMAdmin)
admin.site.register(eraM)
admin.site.register(genreM)
admin.site.register(mainWordM)