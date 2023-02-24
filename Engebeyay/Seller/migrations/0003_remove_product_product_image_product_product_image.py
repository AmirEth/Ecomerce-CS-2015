# Generated by Django 4.1.6 on 2023-02-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0002_rename_stock_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Product_image',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to=''),
        ),
    ]