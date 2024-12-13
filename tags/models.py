from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100,)
    tags = models.ManyToManyField(Tag, related_name='books')
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото фильма', null=True, blank=True)
    price = models.FloatField(verbose_name="Укажите цену книги", default=10)

    def __str__(self):
        return self.name


