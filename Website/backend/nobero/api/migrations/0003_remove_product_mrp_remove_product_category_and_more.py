# Generated by Django 5.1 on 2024-08-25 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_mrp_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='MRP',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fabric',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_7_day_sale',
        ),
        migrations.RemoveField(
            model_name='product',
            name='length',
        ),
        migrations.RemoveField(
            model_name='product',
            name='neck',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sleeve',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='color',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='size',
        ),
    ]
