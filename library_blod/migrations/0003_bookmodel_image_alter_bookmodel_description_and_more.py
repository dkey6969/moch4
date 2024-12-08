# Generated by Django 5.1.3 on 2024-12-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_blod', '0002_alter_bookmodel_description_alter_bookmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='films/', verbose_name='Загрузите фото фильма'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='description',
            field=models.TextField(blank=True, verbose_name='Укажите описания книги'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='укажите названия книги'),
        ),
    ]
