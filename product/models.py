from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            help_text="Nazwa produktu")


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            help_text="Nazwa produktu")
    price = models.IntegerField(
        default=100, null=False, help_text="Cena")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, help_text="Kategoria")

    def __str__(self):
        return self.name


class Zakup(models.Model):
    data = models.DateTimeField(default=timezone.now)


class ZakupProduktu(models.Model):
    zakup = models.ForeignKey(Zakup, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, help_text="Produkt")
