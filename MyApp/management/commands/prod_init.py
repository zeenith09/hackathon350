from django.core.management.base import BaseCommand
from MyApp.models import Product

class Command(BaseCommand):
    help = 'Initialize product data'

    def handle(self, *args, **kwargs):
        products = [
            {'name': 'Eggs', 'price': 2.00},
            {'name': 'Beef', 'price': 1.50},
            {'name': 'Chicken', 'price': 1.55},
            {'name': 'Milk', 'price': 4.50},
            {'name': 'Scooby Snacks', 'price': 0.90},
        ]
        
        Product.objects.all().delete()  # Clear existing products
        
        for product_data in products:
            Product.objects.create(
                name=product_data['name'],
                price=product_data['price']
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully initialized products'))
