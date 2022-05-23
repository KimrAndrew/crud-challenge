from django.test import TestCase
from inventory_manager.models.BaseProduct import BaseProduct


class BaseProductTest(TestCase):
    def test_instantiate_BaseProduct(self):
        expected_item = {
            "item_name": 'Gucci Slides',
            "item_description": 'The coolest slides in town',
            "price": 500,
        }

        product = BaseProduct.objects.create(
            name='Gucci Slides',
            description='The coolest slides in town',
            price=500,
            )

        self.assertEqual(product.name,expected_item["item_name"])
        self.assertEqual(product.description, expected_item["item_description"])
        self.assertEqual(product.price,expected_item["price"])
