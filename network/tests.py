from django.test import TestCase
from datetime import datetime
from .models import Product, MetworkUnit


class ProductModelTest(TestCase):
    def test_product_str_method(self):
        product = Product(name='Test Product', model='Test Model')
        self.assertEqual(str(product), 'Test Product, Test Model')


class MetworkUnitModelTest(TestCase):
    def test_metworkunit_str_method(self):
        metworkunit = MetworkUnit(name='Test MetworkUnit', type='FA', level='0')
        self.assertEqual(str(metworkunit), 'Test MetworkUnit - FA')

    def test_metworkunit_debt_default_value(self):
        metworkunit = MetworkUnit.objects.create(name='Test MetworkUnit', type='FA', level='0')
        self.assertEqual(metworkunit.debt, 0)

    def test_metworkunit_date_create_default_value(self):
        metworkunit = MetworkUnit.objects.create(name='Test MetworkUnit', type='FA', level='0')
        self.assertEqual(metworkunit.date_create.date(), datetime.now().date())
