# Generated by Django 5.1 on 2024-08-22 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MRP', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_7_day_sale', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fit', models.CharField(max_length=100)),
                ('fabric', models.CharField(max_length=100)),
                ('neck', models.CharField(max_length=100)),
                ('sleeve', models.CharField(max_length=100)),
                ('pattern', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_urls', to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_skus', to='api.product')),
            ],
        ),
    ]
