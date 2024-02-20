from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from .models import Customer, Product, Order


logger = logging.getLogger(__name__)


def index(request):
    logger.info('INDEX page raised')
    message = 'Welcome to ShopApp'
    return render(request, 'shopapp/index.html', context={'content': message})


def main(request):
    logger.info('MAIN page raised')
    message = 'Main Page of ShopApp'
    return render(request, 'shopapp/main.html', context={'content': message})


def about(request):
    logger.info('ABOUT page raised')
    message = 'About Page of ShopApp'
    return render(request, 'shopapp/main.html', context={'content': message})


def client_orders(request, phone):
    logger.info('client_order page')
    client = get_object_or_404(Customer, phone=phone)
    orders = Order.objects.filter(customer=client.pk).order_by('pk')
    context = {
        'customer': client,
        'orders': orders,
    }
    return render(request, 'shopapp/client_orders.html', context)


def client_products(request, phone):
    logger.info('client_products page')
    client = get_object_or_404(Customer, phone=phone)
    orders = Order.objects.filter(customer=client.pk).order_by('pk')
    products = [order.products.all() for order in orders]
    context = {
        'customer': client,
        'orders': orders,
        'products': products,
    }
    return render(request, 'shopapp/client_products.html', context)