from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template import loader
from .models import Product, Cart, CartItem

# Create your views here.

def index(request):
  if request.user.is_authenticated:
    products = Product.objects.all().values()
    cart, created = Cart.objects.get_or_create(user=request.user)
    if not created:
        cart.save()
    template = loader.get_template('index.html')
    context = {
        'products': products,
        'cart': cart
    }
    return HttpResponse(template.render(context, request))
  else:
    return JsonResponse({"error": "You must be logged in"}, status=403)

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return JsonResponse({"message": "Item added", "cart_count": cart.get_items().count()})
    else:
        return JsonResponse({"error": "You must be logged in"}, status=403)

def remove_from_cart(request, item_id):
    pass

def view_cart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    template = loader.get_template('cart.html')
    context = {
        'cart': cart
    }
    return HttpResponse(template.render(context, request))

def get_product_price(request, product_id):
    pass

def checkout(request):
    pass
