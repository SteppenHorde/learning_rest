from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    birth_date = models.DateTimeField(verbose_name='Дата рождения')
    country = models.CharField(verbose_name='Страна', max_length=50)

    class Meta:
        ordering = ['last_name', 'country']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    pub_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    title = models.CharField(verbose_name='Название', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    desc = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ['title', 'pub_date', 'author']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
