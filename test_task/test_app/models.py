from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='название книги')
    author_name = models.CharField(max_length=50, verbose_name='автор книги')
    description = models.TextField(verbose_name='Описание книги')

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['-id']
