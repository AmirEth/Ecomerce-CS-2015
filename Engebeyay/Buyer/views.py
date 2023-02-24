from django.shortcuts import render,redirect
from .models import *
import json
from django.http import JsonResponse
# Create your views here.


def store(request):
    products=Product.objects.all()


    context={'products':products}
   
    return render(request, 'Buyer/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        buyer = request.user.buyer
        order, created = Order.objects.get_or_create(buyer=buyer, complete=False)
        items = order.orderitem_set.all()
        
    else:
        
        order = {'get_cart_total':0, 'get_cart_items':0}

    context= {'items': items,'order':order}
    return render(request, 'Buyer/cart.html',context)
def checkout(request):
    context={}
    return render(request, 'Buyer/checkout.html',context)

def updateItem(request):
	if request.user.is_authenticated:
             if request.mathod=='POST':
                  buyer = request.user.buyer
                  order = Order.objects.get(buyer=buyer, complete=False)
                  items = order.orderitem_set.all()     
                  items.delete()
                  return redirect('cart')
                  
             
