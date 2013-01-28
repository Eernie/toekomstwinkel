from API.models import *
from django.core.serializers import serialize
from django.http import HttpResponse
import pprint as pp


def getProduct(request,id=0):
  products = Product.objects.get(EAN=id)
  json = serialize("json", [products,])
  return HttpResponse(json)

def getGroceryList(request, id=0):
  groceryList = GroceryList.objects.get(pk=id)
  groceryListItems = GroceryList_Product.objects.select_related().filter(grocerylist=id)
  groceryList.items = groceryListItems
  json = serialize("json", groceryListItems,relations=('product',))
  return HttpResponse(json)

def boughtProducts(request,products):
  productList = products.split("/")[:-1]
  for productEAN in productList:
    print len(productList)
    product = Product.objects.get(EAN=productEAN)
    product.stock -= 1
    product.save()
  return HttpResponse(productList)