from django.test import TestCase

from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', code='JD123', phone_number='+254700000000')

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.code, 'JD123')
        self.assertEqual(self.customer.phone_number, '+254717886979')

class OrderModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Jane Doe', code='JD456', phone_number='+254717886979')
        self.order = Order.objects.create(customer=self.customer, item='Item 1', amount=100.0)

    def test_order_creation(self):
        self.assertEqual(self.order.customer.name, 'Jane Doe')
        self.assertEqual(self.order.item, 'Item 1')
        self.assertEqual(self.order.amount, 100.0)
