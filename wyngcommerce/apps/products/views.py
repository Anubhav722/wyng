from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from apps.products.models import ProductMaster
import pandas as pd
from django.db import transaction


def blah(request):
    # import ipdb; ipdb.set_trace()
    file_path = '/Users/anubhavsingh/Downloads/FAQ Files/Inputs/Product Master.xlsx'
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        ProductMaster.objects.create(
            sku=row['EANCode'],
            brand=row['Brand'],
            department=row['Department'],
            product_name=row['Product Full Name'],
            mrp=row['Online MRP '],
            selling_price=row['Online MRP '])
    return HttpResponse("ho gya")
