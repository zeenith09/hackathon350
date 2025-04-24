from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template import loader
from .models import Product, Cart, CartItem

# Create your views here.

def index(request):
  products = Product.objects.all().values()
  cart = Cart.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'products': products,
    'cart': cart
  }
  return HttpResponse(template.render(context, request))

def add_to_cart(request, product_id):
    pass

def remove_from_cart(request, item_id):
    pass

def view_cart(request):
    cart = Cart.objects.all().values()
    template = loader.get_template('cart.html')
    context = {
        'cart': cart
    }
    return HttpResponse(template.render(context, request))

def get_product_price(request, product_id):
    pass

def checkout(request):
    pass
