# Generated by Django 2.2.23 on 2021-06-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210601_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=100, help_text='Cena'),
        ),
        migrations.AlterField(
            model_name='zakup',
            name='quantity',
            field=models.FloatField(default=1.0, help_text='ilość'),
        ),
    ]
