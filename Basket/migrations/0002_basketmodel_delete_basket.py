# Generated by Django 5.1.3 on 2024-12-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='Puskin1@gmail.com', max_length=100, verbose_name='укажите почту автора')),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
    ]
