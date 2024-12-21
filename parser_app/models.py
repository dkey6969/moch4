from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    availability = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return self.title
