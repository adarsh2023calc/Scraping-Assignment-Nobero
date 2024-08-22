from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=100)
    url = models.URLField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    MRP = models.DecimalField(max_digits=10, decimal_places=2)
    last_7_day_sale = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fit = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    neck = models.CharField(max_length=100)
    sleeve = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class SKU(models.Model):
    product = models.ForeignKey(Product, related_name='available_skus', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.color} - {self.size}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_urls', on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return self.image_url
