from django.conf.urls import url, include
from .views import all_products, get_actions


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', get_actions, name='actions'),
    ]