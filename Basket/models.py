from django.db import models
from library_blod.models import BookModel


class BasketModel(models.Model):
    CHECKING = (
        ('✅', '✅'),
        ('❌', '❌')
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, verbose_name="укажите почту автора", default='Puskin1@gmail.com')
    phone_number = models.CharField(max_length=100)
    choice_check = models.CharField(max_length=10, choices=CHECKING, null=True, blank=True)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name="baskets",blank=True, null=True)


    def __str__(self):
        return self.name






