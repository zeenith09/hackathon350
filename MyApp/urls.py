from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # TBA once fill out views
]
