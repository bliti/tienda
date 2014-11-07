from django.db import models
import decimal


class Product(models.Model):
    """
    Defines each product to be sold in the store.
    Tracks its own inventory and shipping.
    
    Product images are saved in the static folder
    due to how heroku does not allow file uploads.
    
    Rather than introduce additional dependencies
    I decided to just put the images in the static
    files folder and serve them from there. The default
    is to NOT serve them from static.
    
    You can also upload the images to any host and
    save the asset URL with the product. Set the field 
    serve_image_from_static to True and the product template
    will do the rest.
    
    There is one image per product, because this
    is a simple store. There is a video link field
    that you can use if you want to show more stuff
    through a video.
    
    Images are not required by default. Due to how
    no every product requires an image.
    
    Price and shipping are in cents. This to comply with how stripe.com
    handles charges. Example: 24.95 would be 2495.
    """
    sku = models.IntegerField(unique=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    shipping = models.IntegerField()
    name = models.CharField(max_length=140)
    description = models.TextField() 
    ships_to = models.TextField()
    image = models.TextField(null=True, blank=True)
    serve_image_from_static = models.BooleanField(default=False)
    video_link = models.URLField(null=True, blank=True)


    def __unicode__(self):
        return self.name


    @property
    def price_with_shipping(self):
        return self.price + self.shipping
    
    
    @property
    def price_as_decimal(self):
        return decimal.Decimal(self.price) / 100
    
    
    @property
    def shipping_as_decimal(self):
        return decimal.Decimal(self.shipping) / 100