from django.urls import path
from django.conf.urls import url
from .views import StoreRudView,StoreCreateView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', StoreRudView.as_view(), name='store-rud'),
    url(r'^$', StoreCreateView.as_view(), name='store-create'),

]
