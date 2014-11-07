from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.core.urlresolvers import reverse
from product.models import Product


"""
Note: You should go ahead and do your own integration tests
with selenium or something like it.
This merely makes sure the pages run and respond properly..
It does not test style or layout.
"""


class StoreProductListIndexPageTest(TestCase):


    def setUp(self):
        self.client = Client()
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
    
    
    def test_store_index_page_request_returns_200(self):
        response = self.client.get(reverse('store_index'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_company_name_in_store_index_page(self):
        response = self.client.get(reverse('store_index'))
        self.assertTrue(settings.COMPANY_NAME in response.content)


    def test_store_index_page_has_product_list(self):
        response = self.client.get(reverse('store_index'))
        self.assertTrue('Products' in response.content)

    
    def test_store_index_page_product_list_has_product(self):
        product_url = reverse('product_detail', kwargs={'pk': self.product.pk})
        response = self.client.get(reverse('store_index'))
        self.assertTrue(product_url in response.content)


class StoreProductDetailPageTest(TestCase):
    
    
    def setUp(self):
        self.client = Client()
        
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
    
    
    def test_store_product_detail_page(self):
        response = self.client.get(reverse('product_detail', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200 )
    
    
    def test_store_product_detail_has_product_name(self):
        response = self.client.get(reverse('product_detail', kwargs={'pk': self.product.pk}))
        self.assertTrue(self.product.name in response.content)