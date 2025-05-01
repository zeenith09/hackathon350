from django.contrib import admin
from MyApp.models import Product, Cart, CartItem

# Custom Classes
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity",)

class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at",)

#Register models
admin.site.register(Product)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)