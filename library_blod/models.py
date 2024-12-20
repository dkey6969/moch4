from symtable import Class

from django.db import models
from django.db.models import Model


class BookModel(models.Model):
    GENRE = (
        ('Ужасы','Ужасы'),
        ('Комедия','Комедия'),
        ('Приключения','Приключения'),
        ('Фантастика','Фантастика')
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото фильма',null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name="укажите названия книги")
    description = models.TextField(verbose_name="Укажите описания книги", blank=True)
    price = models.FloatField(verbose_name="Укажите цену книги", default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Фантастика')
    gmail = models.CharField(max_length=100, verbose_name="укажите почту автора", default='Puskin1@gmail.com')
    director = models.CharField(max_length=100, verbose_name="Укажите автора", default="Пушкин")
    trailer = models.URLField(verbose_name='укажите ссылку трейлера фильма', null=True)



    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')

    )
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    text = models.TextField(verbose_name='напишите отзыв о книге')
    stars = models.CharField(max_length=100, choices=STARS, verbose_name='поставьте оценку', default='⭐')

    def __str__(self):
        return f'{self.book}:{self.stars}'

