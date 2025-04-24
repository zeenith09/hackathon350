from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.view_cart, name='cart')
]
urlpatterns += staticfiles_urlpatterns()
### To run needa also do prod_init since we added it as a command
# python manage.py makemigrations
# python manage.py migrate
# python manage.py prod_init
# python manage.py runserver
# Need to fill out views, style.css, app.js, and index.html
###
