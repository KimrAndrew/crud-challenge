from django.test import TestCase
from inventory_manager.models.BasicProduct import BasicProduct


class InventoryItemTest(TestCase):
    def test_instantiate_BasicProduct(self):
        expected_item = {
            "item_name": 'Gucci Slides',
            "item_description": 'The coolest slides in town',
            "price": 500,
            "quantity": 600
        }

        product = BasicProduct.objects.create(
            name='Gucci Slides',
            description='The coolest slides in town',
            price=500,
            quantity= 600,
            )

        self.assertEqual(product.name,expected_item["item_name"])
        self.assertEqual(product.description, expected_item["item_description"])
        self.assertEqual(product.price,expected_item["price"])
        self.assertEqual(product.quantity,expected_item['quantity'])
