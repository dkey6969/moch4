# Generated by Django 5.1.3 on 2024-12-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basket', '0003_basketmodel_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketmodel',
            name='choice_check',
            field=models.CharField(blank=True, choices=[('✅', '✅'), ('❌', '❌')], max_length=10, null=True),
        ),
    ]
