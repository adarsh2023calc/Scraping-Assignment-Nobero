# products/management/commands/load_products.py

import json
from django.core.management.base import BaseCommand
from api.models import Product


class Command(BaseCommand):
    help = 'Load products from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file containing product data')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            products = json.load(file)

            for product_data in products:
                Product.objects.create(
                    category=product_data['category'],
                    url=product_data['url'],
                    title=product_data['title'],
                    price=product_data['price'],
                    MRP=product_data['MRP'],
                    last_7_day_sale=product_data.get('last_7_day_sale'),  # Use .get to avoid KeyError
                    fit=product_data['fit'],
                    fabric=product_data['fabric'],
                    neck=product_data['neck'],
                    sleeve=product_data['sleeve'],
                    pattern=product_data['pattern'],
                    length=product_data['length'],
                    description=product_data['description']

                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded products from JSON file'))