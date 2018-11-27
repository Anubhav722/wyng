from django.db import models

# from apps.common.models import TenantAwareModel
# Create your models here.


class ProductMaster(models.Model):
    """docstring for ProductMaster"""
    sku = models.CharField(max_length=120)
    brand = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    product_name = models.CharField(max_length=200)
    mrp = models.CharField(max_length=10)
    selling_price = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name + " ---> " + self.sku
