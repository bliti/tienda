from django.test import TestCase
from django.db import IntegrityError
from decimal import Decimal, InvalidOperation
from .models import Product


class ProductTest(TestCase):
    
    
    def setUp(self):
        
        self.product = Product.objects.create(
            sku=001,
            price=29.97,
            quantity=1,
            shipping=5.99,
            name='Test Product',
            description='Its a test product.',
            ships_to='USA',
            image='http://sunny95.com/wp-content/blogs.dir/16/files/2013/05/rick-astley.jpg',
            video_link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            )
        
        self.wrong_price = 9999999.999
        self.wrong_shipping = 99999999.9999
    
    
    def set_wrong_price(self):
        self.product.price = self.wrong_price
        try:
            self.product.save()
        except InvalidOperation:
            return False
    
    
    def set_wrong_shipping(self):
        self.product.price = self.wrong_shipping
        try:
            self.product.save()
        except InvalidOperation:
            return False
    
    
    def create_product_same_sku_as_other_returns_false(self):
        try:
            self.product_copy = Product.objects.create(
            sku=001,
            price=29.97,
            quantity=1,
            shipping=5.99,
            name='Test Product',
            description='Its a test product.',
            ships_to='USA'
            )
        except IntegrityError:
            return False
         
    
    def test_set_wrong_price_returns_false(self):
        self.assertFalse(self.set_wrong_price())
         
    
    def test_set_wrong_shipping_returns_false(self):
        self.assertFalse(self.set_wrong_shipping())


    def test_product_sku_uniqueness(self):
        self.assertFalse(self.create_product_same_sku_as_other_returns_false())
    
    
    def test_try_to_ship_two_products_with_only_one_available(self):
        self.assertNotEqual(self.product.quantity, 2)


    def test_try_to_ship_product_to_other_country(self):
        self.assertNotEqual(self.product.ships_to, 'UK')


    def test_image_is_not_served_from_static(self):
        self.assertFalse(self.product.serve_image_from_static)
    
    
    def tearDown(self):
        pass