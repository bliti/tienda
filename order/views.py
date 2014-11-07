from django.views.generic import View
from .models import OnlineOrder
#import stripe


class OnlineOrderView(View):
    """
    Creates an order and makes the stripe charge.
    """
    
    
    
    def post(self, request, *args, **kwargs):
        pass
        