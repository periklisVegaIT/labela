from django.db import models

class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    price = models.IntegerField()

class CartItem(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)