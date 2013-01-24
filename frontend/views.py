from API.models import Product,GroceryList
from django.shortcuts import render_to_response

def home(request):
  p = Product.objects.all()

  return render_to_response('frontend/home.html', {'products':p})

def cart(request):
  if not request.session.__contains__('groceryid'):
    glist = GroceryList() 
    glist.save()
    request.session['groceryid'] = glist.id
  else:
    glist = GroceryList.objects.get(id=request.session.get('groceryid'))




  return render_to_response('frontend/cart.html', {'grocerylist':glist})