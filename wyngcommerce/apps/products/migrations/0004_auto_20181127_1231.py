# Generated by Django 2.1.3 on 2018-11-27 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181127_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmaster',
            name='product_attribute',
        ),
        migrations.AddField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductMaster'),
        ),
    ]
