from django.core.management.base import BaseCommand, CommandParser
from myhw1app.models import Customer, Order


class Command(BaseCommand):
    help = "Get orders by customer phone number"

    def add_arguments(self, parser):
        parser.add_argument('phone', type=str, help='Phone Number')

    def handle(self, *args, **kwargs):
        phone = kwargs.get('phone')
        customer = Customer.objects.filter(phone=phone).first()
        if customer is not None:
            orders = Order.objects.filter(customer=customer)
            self.stdout.write(f'{orders}')
        else:
            self.stdout.write(f'{customer}')