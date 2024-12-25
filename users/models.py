from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    LEVELS = (
        ('jun', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    )

    phone_number = models.CharField(max_length=14)
    level = models.CharField(max_length=10, choices=LEVELS, default='jun')
    salary = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.level == 'jun':
            self.salary = 700
        elif self.level == 'middle':
            self.salary = 1000
        elif self.level == 'senior':
            self.salary = 2000
        else:
            raise ValueError("Недопустимый уровень")

        super().save(*args, **kwargs)

