from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100,)
    tags = models.ManyToManyField(Tag, related_name='books')

    def __str__(self):
        return self.name


