from API.models import Product,GroceryList, GroceryList_Product
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse

def home(request):
  p = Product.objects.all().order_by('name')

  return render_to_response('frontend/home.html', {'products':p})

def cart(request):
  if not request.session.__contains__('groceryid'):
    glist = GroceryList() 
    glist.save()
    request.session['groceryid'] = glist.id
  else:
    glist = GroceryList.objects.get(id=request.session.get('groceryid'))

  return render_to_response('frontend/cart.html', {'grocerylist':glist})

def addtocart(request,prodid):
  glist = GroceryList.objects.get(id=request.session.get('groceryid'))
  product = Product.objects.get(id=prodid)

  grocerylistRow = GroceryList_Product.objects.filter(product=product,grocerylist=glist)

  if not grocerylistRow:
    temp = GroceryList_Product.objects.create(product=product,grocerylist=glist,amount=1)
  else:
    temp = grocerylistRow[0]
    temp.amount += 1

  temp.save()

  return HttpResponse()

def clear(request):
  del request.session['groceryid']

  return redirect('/')
