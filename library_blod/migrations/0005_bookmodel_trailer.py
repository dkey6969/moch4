# Generated by Django 5.1.3 on 2024-12-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_blod', '0004_alter_bookmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='trailer',
            field=models.URLField(null=True, verbose_name='укажите ссылку трейлера фильма'),
        ),
    ]
