from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/<int:cart_id>/', views.view_cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart')
]
urlpatterns += staticfiles_urlpatterns()
### To run needa also do prod_init since we added it as a command
# python manage.py makemigrations
# python manage.py migrate
# python manage.py prod_init
# python manage.py runserver
# Need to fill out views, style.css, app.js, and index.html
###
