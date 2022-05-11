from django.test import TestCase
from inventory_manager.models.Customer import Customer

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
            name='Slides',
            description='The coolest slides in town',
            price=500,
            quantity= 600,
            manufacturer = manufacturer
            )

        self.assertEqual(item.name,item_name)
        self.assertEqual(item.description, item_description)
        self.assertEqual(item.price,price)
        self.assertEqual(item.quantity,quantity)
        self.assertEqual(item.manufacturer,manufacturer)

class CustomerTest(TestCase):
    def test_instantiate_customer(self):
        customer_first_name = 'P'
        customer_last_name='Sherman'
        customer_address='42 Wallaby Way, Sydney'
        customer = Customer(first_name='P', last_name='Sherman', address='42 Wallaby Way, Sydney')

        self.assertEqual(customer.first_name, customer_first_name)
        self.assertEqual(customer.last_name, customer_last_name)
        self.assertEqual(customer.address, customer_address)
