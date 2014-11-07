from django.conf.urls import patterns, url
from .views import OnlineOrderCreate

urlpatterns = patterns('',
    url(r'^order/$', OnlineOrderCreate.as_view(), name="create_online_order"),
)