from API.models import Product, GroceryList
from django.core.serializers import serialize
from django.http import HttpResponse

def home(request):

    return HttpResponse("Hallo Wereld! %s %s <br> %s" % (request.method, request.GET, vars(request)))

def getProduct(request,id=0):
    products = Product.objects.get(EAN=id)
    json = serialize("json", [products,])
    return HttpResponse(json)

def getGroceryList(request, id=0):
    groceryList = GroceryList.objects.filter(id=id)
    json = serialize("json", groceryList, relations=('products',))
    return HttpResponse(json)