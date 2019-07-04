from datetime import datetime
from django.db import models


#  отрицательные годы это B.C.
CURRENT_YEAR = datetime.now().year
YEARS = [
    (
        year,
        str(year) if year >= 0 else f'{str(year)[1:]} B.C.'
    )
    for year in range(CURRENT_YEAR, -1001, -1)
]


#  для поля с годом достаточно CharField, DateField сохраняет избыточные поля
class Author(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    birth_year = models.CharField(
        verbose_name='Год рождения',
        choices=YEARS[10:],  # убираем слишком молодых авторов
        default=YEARS[10],
        max_length=9,  # len(YYYY B.C.) -> 9
    )
    country = models.CharField(verbose_name='Страна', max_length=50)

    class Meta:
        ordering = ['last_name', 'country']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


#  для поля с годом достаточно CharField, DateField сохраняет избыточные поля
class Book(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)
    pub_year = models.CharField(
        verbose_name='Дата публикации',
        choices=YEARS,
        default=CURRENT_YEAR,
        max_length=9,  # len(YYYY B.C.) -> 9
    )

    class Meta:
        ordering = ['title', 'pub_year', 'author']

    def __str__(self):
        return f'{self.title} ({self.author})'
