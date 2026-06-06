from django.test import TestCase
from django.contrib.auth.models import User
from .models import Client, Product, Order, OrderStatus
from .utils import calculate_order_cost
from decimal import Decimal

class OrderCostCalculationTest(TestCase):
    def test_calculate_order_cost(self):
        # Создаём тестовые данные
        client = Client.objects.create(name="Тестовый клиент")
        product = Product.objects.create(
            name="Тестовая продукция",
            base_material_cost=Decimal('10.00'),
            base_time_norm_hours=Decimal('2.00')
        )
        status = OrderStatus.objects.create(name="Новый")
        
        order = Order.objects.create(
            client=client,
            product=product,
            quantity=100,
            deadline_date='2025-12-31',
            status=status,
            total_cost=0
        )
        
        # Рассчитываем себестоимость
        cost = calculate_order_cost(order)
        
        # Ожидаемая себестоимость: 100 * 10 + 2 * 1000 = 1000 + 2000 = 3000
        self.assertEqual(cost, Decimal('3000.00'))

class OrderCreationTest(TestCase):
    def test_order_creation(self):
        client = Client.objects.create(name="Клиент 1")
        product = Product.objects.create(name="Продукт 1", base_material_cost=100, base_time_norm_hours=1)
        status = OrderStatus.objects.create(name="Новый")
        
        order = Order.objects.create(
            client=client,
            product=product,
            quantity=50,
            deadline_date='2025-12-31',
            status=status
        )
        
        self.assertEqual(order.client.name, "Клиент 1")
        self.assertEqual(order.quantity, 50)