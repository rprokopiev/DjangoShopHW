from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('client_orders/<str:phone>', views.client_orders, name='client_orders'),
]