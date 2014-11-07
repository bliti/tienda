from django.conf.urls import patterns, url
from .views import ProductList

urlpatterns = patterns('',
    url(r'^$', ProductList.as_view(), name="store_index_product_list"),
)