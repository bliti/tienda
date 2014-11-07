from django.views.generic import ListView, DetailView
from django.conf import settings
from product.models import Product


class ProductList(ListView):
    model = Product
    company_name = settings.COMPANY_NAME


class ProductDetail(DetailView):
    pass