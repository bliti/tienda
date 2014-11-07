from django.conf.urls import patterns, url
from .views import ProductList, ProductDetail

urlpatterns = patterns('',
    url(r'^$', ProductList.as_view(), name="store_index_product_list"),
    url(r'^product/(?P<pk>\d+)/$', ProductDetail.as_view(), name='product_detail'),
)