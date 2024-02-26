from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('client_orders/<str:phone>', views.client_orders, name='client_orders'),
    path('client_products/<str:phone>', views.client_products, name='client_products'),
    path('inventory/', views.inventory, name='inventory'),
    path('add_product/', views.add_product, name='add_product'),   
]