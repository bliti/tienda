from django.db import models


class Product(models.Model):
    """
    Defines each product to be sold in the store.
    Tracks its own inventory and shipping.
    """
    
    sku = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    shipping = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=140)
    description = models.TextField() 
    ships_to = models.TextField()
    
    
    #NOTE: images for the product will be handled
    # by another object and referenced 1-1. 