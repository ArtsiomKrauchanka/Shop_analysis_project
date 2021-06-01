from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            help_text="Nazwa produktu")


class Product(models.Model):
    name = models.CharField(max_length=200, unique=False,
                            help_text="Nazwa produktu")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, help_text="Kategoria")

    def __str__(self):
        return self.name


class Zakup(models.Model):
    data = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, help_text="Produkt")
    price = models.FloatField(
        default=100, null=True, help_text="Cena")
    quantity = models.FloatField(
        default=1.0, null=True, help_text="ilość")
