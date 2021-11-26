from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_products, name='catalog_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
]
