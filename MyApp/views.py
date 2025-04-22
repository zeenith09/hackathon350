from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, Cart, CartItem

# Create your views here.

def index(request):
    pass

def add_to_cart(request, product_id):
    pass

def remove_from_cart(request, item_id):
    pass

def view_cart(request):
    pass

def get_product_price(request, product_id):
    pass

def checkout(request):
    pass
