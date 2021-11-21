from django.shortcuts import render
from .models import storeCategory, storeProduct

def catalog_products(request):
    products = storeProduct.objects.all()
    return render(request, 'catalog/homepage.html', {'products': products})