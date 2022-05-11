from django.test import TestCase

from inventory_manager.models.Inventory_Item import Inventory_Item
from .models.Manufacturer import Manufacturer

# Create your tests here.
class ManufacturerTestCase(TestCase):
    def test_instantiate_manufacturer(self):
        gucci = Manufacturer.objects.create(name='Gucci')
        nike = Manufacturer.objects.create(name='Nike')
        self.assertEquals(gucci.name, 'Gucci')
        self.assertEqual(nike.name, 'Nike')

class InventoryItemTest(TestCase):
    def test_instantiate_Inventory_Item(self):
        manufacturer = Manufacturer.objects.create(name='Gucci')

        item_name = 'Slides'
        item_description = 'The coolest slides in town'
        price = 500
        quantity = 600

        item = Inventory_Item.objects.create(
            name=item_name,
            description=item_description,
            price=price,
            quantity= quantity,
            manufacturer = manufacturer
            )
            
        self.assertEqual(item.name,item_name)
        self.assertEqual(item.description, item_description)
        self.assertEqual(item.price,price)
        self.assertEqual(item.quantity,quantity)
        self.assertEqual(item.manufacturer,manufacturer)
