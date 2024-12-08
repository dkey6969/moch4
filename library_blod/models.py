from django.db import models

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



