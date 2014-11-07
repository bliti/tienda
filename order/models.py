from django.db import models
from product.models import Product


class OnlineOrder(models.Model):
    """
    Defines a product order object.
    The customer information
    and product information
    are stored here.
    
    Only one product per order 
    at the moment, becuase this project
    lacks a shopping cart. On purpose.
    """
    
    email = models.EmailField()
    name = models.TextField()
    product = models.ForeignKey('product.Product')
    date = models.DateTimeField(auto_now_add=True)
    stripe_token = models.TextField()
    shipping_address = models.TextField()
    email_confirmed = models.BooleanField(default=False)