from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.json

# Create your views here.
from apps.products.models import ProductMaster, ProductAttribute
import pandas as pd
from django.db import transaction

import time

attr_header = ['Style Code', 'Colour code', 'Colour   ', 'Size', 'Garment Type', 'Fabric Pattern Detail', 'Age', 'Toon Lable', 'Fabric content', 'Gsm']

def blah(request):
    # import ipdb; ipdb.set_trace()
    file_path = '/Users/govindsharma/Downloads/FAQ Files/Inputs/Product Master.xlsx'
    for i in range(1):
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            x = ProductMaster.objects.create(
                sku=row['EANCode'],
                brand=row['Brand'],
                department=row['Department'],
                product_name=row['Product Full Name'],
                mrp=row['Online MRP '],
                selling_price=row['Salesprice'],
                purchase_unit=row['Purchase Unit'],
                seasons_collection=row['Market Division name'])

            for attr in attr_header:
                ProductAttribute.objects.create(
                        attr_name=attr,
                        attr_type='',
                        attr_value=row[attr],
                        product=x
                    )

    return HttpResponse("ho gya")


def time_taken(request):
    start_time = time.time()
    x = ProductMaster.objects.filter(brand__icontains="nike")
    y = x.filter(sku="8907074000009")
    z = ProductMaster.objects.filter(department__icontains="ladies")
    u = ProductMaster.objects.filter(department__icontains="kids")
    q = ProductMaster.objects.filter(product_name__icontains="woven")
    # mrp = ProductMaster.objects.filter()
    mrp = ProductMaster.objects.filter(mrp__gte="150") \
                    .extra({'mrp_uint': "CAST(mrp as UNSIGNED)"}) \
                    .order_by('-mrp_uint')
    end_time = time.time()
    return JsonResponse({"time": end_time - start_time,
                         "data": {"n": x.count(),
                                  "sku": y.count(),
                                  "ladies": z.count(),
                                  "kids": u.count(),
                                  "product_name": q.count(),
                                  "mrp": mrp.count()}})
