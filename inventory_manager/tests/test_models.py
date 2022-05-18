from django.test import TestCase
from inventory_manager.models.Inventory_Item import InventoryItem


class InventoryItemTest(TestCase):
    def test_instantiate_Inventory_Item(self):
        expected_item = {
            "item_name": 'Gucci Slides',
            "item_description": 'The coolest slides in town',
            "price": 500,
            "quantity": 600
        }

        item = InventoryItem.objects.create(
            name='Gucci Slides',
            description='The coolest slides in town',
            price=500,
            quantity= 600,
            )

        self.assertEqual(item.name,expected_item["item_name"])
        self.assertEqual(item.description, expected_item["item_description"])
        self.assertEqual(item.price,expected_item["price"])
        self.assertEqual(item.quantity,expected_item['quantity'])

# TODO Add Tests for Views