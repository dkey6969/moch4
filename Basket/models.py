from django.db import models
from library_blod.models import BookModel

class Basket(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    email = models.EmailField(verbose_name="Электронная почта клиента")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона клиента")
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, verbose_name="Выбранная книга")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.name} - {self.book.title}"
