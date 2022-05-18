from django.db import models
#eraM,genreM,AboutM,mainWordM,ArticleM

# Create your models here.
class eraM(models.Model):#要約＿年代
    era=models.CharField(max_length=30,default=' 年～')
    def __str__(self):
        return str(self.era)

class genreM(models.Model):#要約＿ジャンル
    genre=models.CharField(max_length=30,default='WH')
    def __str__(self):
        return str(self.genre)

class AboutM(models.Model):#要約＿A＋B
    genre = models.ForeignKey(genreM, on_delete=models.PROTECT, related_name="genre_about", null=True, blank=True)
    title=models.ForeignKey(eraM,on_delete=models.PROTECT,related_name="era_about",null=True,blank=True)
    text = models.TextField('要約')
    textMore=models.TextField('common')
    create_at = models.DateField('作成日',auto_now_add=True)
    update_at= models.DateField('更新日',auto_now=True)
    def __str__(self):
        return '(' + str(self.genre) + ')' + str(self.title)
    class Meta:
        verbose_name='要約2'
        verbose_name_plural='要約3'

#**********************************************************************************
class mainWordM(models.Model):#要約 から　mainWord を
    mainword=models.CharField(max_length=20,default='noWord')
    madeby=models.CharField(max_length=30,default='anonymous')
    def __str__(self):
        return str(self.mainword)


class ArticleM(models.Model):#要約＿mainWord から　Detail
    title=models.ForeignKey(mainWordM,on_delete=models.CASCADE,related_name="mainword_article",null=True,blank=True)
    text = models.TextField('記事')
    create_at = models.DateField('作成日',auto_now_add=True)
    update_at= models.DateField('更新日',auto_now=True)
    def __str__(self):
        return '(' + str(self.update_at) + ')' + str(self.title)
    class Meta:
        verbose_name='記事'
        verbose_name_plural='記事'