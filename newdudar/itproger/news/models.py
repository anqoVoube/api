from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey


class Reviews(models.Model):
    user = models.CharField(max_length=50)
    timedate = models.DateTimeField()
    text = models.TextField(max_length=300)
    articles = models.ForeignKey('Articles', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Body')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


