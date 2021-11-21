from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_products, name='catalog_products'),
]