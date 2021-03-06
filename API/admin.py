from django.contrib import admin
from API.models import GroceryList, Product, GroceryList_Product

class GroceryList_ProductInline(admin.TabularInline):
    model = GroceryList_Product
    extra = 0

class ProductInline(admin.ModelAdmin):
	inlines = [GroceryList_ProductInline]

class GroceryListInline(admin.ModelAdmin):
	inlines = [GroceryList_ProductInline]


admin.site.register(GroceryList, GroceryListInline)
admin.site.register(Product, ProductInline)