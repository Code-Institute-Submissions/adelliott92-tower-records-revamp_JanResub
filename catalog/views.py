from django.shortcuts import get_object_or_404, render
from .models import storeCategory, storeProduct

def categories(request):
    return {
        'categories': storeCategory.objects.all()
    }

def catalog_products(request):
    products = storeProduct.objects.all()
    return render(request, 'catalog/homepage.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(storeProduct, slug=slug, product_in_stock=True)
    return render(request, 'catalog/products/product_detail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(storeCategory, slug=category_slug)
    products = storeProduct.objects.filter(category=category)
