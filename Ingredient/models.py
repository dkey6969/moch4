from django.db import models
from Recipe.models import RecipeModel

class IngredientModel(models.Model):
    UNIT_CHOICES = [
        ('граммы', 'граммы'),
        ('килограммы', 'килограммы'),
        ('миллилитры', 'миллилитры'),
        ('литры', 'литры'),
        ('штуки', 'штуки'),
    ]

    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
