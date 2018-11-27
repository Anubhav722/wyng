from django.db import models

# Create your models here.


class SubCategory(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    attr_value = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return self.name

