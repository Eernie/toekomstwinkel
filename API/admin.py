from django.contrib import admin
from API.models import GroceryList, Product, GroceryList_Product

class GroceryList_ProductInline(admin.TabularInline):
    model = GroceryList_Product
    extra = 0

class ProductInline(admin.TabularInline):
	inlines = (GroceryList_ProductInline,)

class GroceryListInline(admin.TabularInline):
	inlines = (GroceryList_ProductInline,)

admin.site.register(Product, ProductInline)
admin.site.register(GroceryList, GroceryListInline)