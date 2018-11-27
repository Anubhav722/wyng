from django.db import models
from apps.category.models import Category, SubCategory

# from apps.common.models import TenantAwareModel
# Create your models here.


class ProductMaster(models.Model):
    """docstring for ProductMaster"""
    sku = models.CharField(max_length=120, null=True, blank=True)
    brand = models.CharField(max_length=150, null=True, blank=True)
    department = models.CharField(max_length=150, null=True, blank=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    mrp = models.CharField(max_length=10, null=True, blank=True)
    selling_price = models.CharField(max_length=10, null=True, blank=True)
    purchase_unit = models.CharField(max_length=10, null=True, blank=True)
    seasons_collection = models.CharField(max_length=120, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.product_name + " ---> " + self.sku


class ProductAttribute(models.Model):
    attr_name = models.CharField(max_length=150, null=True, blank=True)
    attr_type = models.CharField(max_length=100, null=True, blank=True)
    attr_value = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.attr_name