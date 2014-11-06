from django.db import models


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
    """
    sku = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    shipping = models.DecimalField(max_digits=6, decimal_places=2)
    name = models.CharField(max_length=140)
    description = models.TextField() 
    ships_to = models.TextField()
    image = models.TextField(null=True)
    serve_image_from_static = models.BooleanField(default=False)
    video_link = models.URLField(null=True)


    def __unicode__(self):
        return self.name