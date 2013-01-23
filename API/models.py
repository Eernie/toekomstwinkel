from django.db import models


class Product(models.Model):
    EAN = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name

class GroceryList(models.Model):
    id = models.AutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through="GroceryList_Product")

class GroceryList_Product(models.Model):
    product = models.ForeignKey(Product)
    grocerylist = models.ForeignKey(GroceryList)
    amount = models.PositiveIntegerField();
