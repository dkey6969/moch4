# Generated by Django 5.1.3 on 2024-12-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='films/', verbose_name='Загрузите фото фильма'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=10, verbose_name='Укажите цену книги'),
        ),
    ]
