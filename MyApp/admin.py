from django.contrib import admin
from MyApp.models import Product, Cart, CartItem

# Custom Classes
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity",)

#Register models
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)