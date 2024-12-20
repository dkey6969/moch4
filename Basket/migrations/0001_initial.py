# Generated by Django 5.1.3 on 2024-12-14 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library_blod', '0006_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя клиента')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта клиента')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона клиента')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_blod.bookmodel', verbose_name='Выбранная книга')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
