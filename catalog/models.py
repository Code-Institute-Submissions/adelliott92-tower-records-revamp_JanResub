from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class storeCategory(models.Model):
    category_Name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_Name

class storeProduct(models.Model):
    category = models.ForeignKey(storeCategory, related_name='product', on_delete=models.CASCADE)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    product_title = models.CharField(max_length=255)
    author_id = models.CharField(max_length=255, default='Administrator')
    description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    product_price = models.DecimalField(max_digits=4, decimal_places=2)
    product_in_stock = models.BooleanField(default=True)
    product_is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_on',)
    
    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.slug])

    def __str__(self):
        return self.product_title
