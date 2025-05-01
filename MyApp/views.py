from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template import loader
from .models import Product, Cart, CartItem

# Create your views here.

def index(request):
    products = Product.objects.all() # rm .values() so template can get product models attribute
    cart, created = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None)
    if not created:
        cart.save()
    template = loader.get_template('index.html')
    context = {
        'products': products,
        'cart': cart
    }

    return HttpResponse(template.render(context, request))

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # anon cart
    cart, created = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return JsonResponse({"message": "Item added", "cart_count": cart.get_items().count(), "new_item": created, "id": cart_item.id, "name": cart_item.product.name, "price": cart_item.product.price, "quantity": cart_item.quantity})

def remove_from_cart(request, cart_item_id):
    cart = get_object_or_404(Cart, user=request.user if request.user.is_authenticated else None)
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    # In theory we dont need to check that cart and cart_item are valid because the get_object_or_404 function does that for us
    try:
        cart_item.delete()
        cart.save()
    except Exception as ex:
        return JsonResponse({"stats": "error", "message": str(ex)}, status=500)
    else:
        return JsonResponse({"message": "Item removed", "cart_count": cart.get_items().count()})

def view_cart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    template = loader.get_template('cart.html')
    context = {
        'cart': cart
    }
    return HttpResponse(template.render(context, request))

def get_product_price(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return JsonResponse({
        'name': product.name,
        'price': float(product.price)
    })

def checkout(request):
    cart = get_object_or_404(Cart, user=request.user if request.user.is_authenticated else None)
    cart_items = cart.get_items()
    
    if request.method == 'POST':
        # process ord + clear cart after checkout
        CartItem.objects.filter(cart=cart).delete()
        return JsonResponse({'success': True, 'message': 'Order completed!'})
    
    if not cart_items: # mt cart
        template = loader.get_template('checkout.html')
        context = {
            'cart': cart,
            'cart_items': [],
            'total': 0
        }
        return HttpResponse(template.render(context, request))
    
    total = cart.get_total_price()
    
    template = loader.get_template('checkout.html')
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total': total
    }
    return HttpResponse(template.render(context, request))
