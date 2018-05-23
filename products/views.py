from django.shortcuts import render
from .models import Product



# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def get_actions(self, request):
    actions = super().get_actions(request)
    if 'delete_selected' in actions:
        del actions['delete_selected']
    return actions