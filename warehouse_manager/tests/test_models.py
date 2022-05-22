from django.test import TestCase
from ..models import Warehouse, WarehouseInventoryItem
from inventory_manager.models.BasicProduct import BasicProduct

class WarehouseTestCase(TestCase):
    def test_instantiate_warehouse(self):
        expected_data = {"location":"Seattle"}
        warehouse = Warehouse.objects.create(location="Seattle")
        self.assertEqual(warehouse.location, expected_data["location"])

class WarehouseItemTestCase(TestCase):

    def setUp(self) -> None:
        self.global_coffee = BasicProduct(
            name="coffee",
            description="bitter",
            quantity = 500,
            price = 6
        )
        self.seattle = Warehouse(location = "Seattle")
        self.tacoma = Warehouse(location="Tacoma")
        self.seattle_coffee = WarehouseInventoryItem(warehouse=self.seattle, item=self.global_coffee)
        self.tacoma_coffee = WarehouseInventoryItem(warehouse=self.tacoma, item=self.global_coffee)

    def test_instantiate_WarehouseItem(self):
        seattle_coffee = WarehouseInventoryItem(warehouse=self.seattle, item=self.global_coffee)
        self.assertEqual(seattle_coffee.warehouse, self.seattle)
        self.assertEqual(seattle_coffee.item, self.global_coffee)
        self.assertEqual(seattle_coffee.warehouse_inventory, 0)
        self.assertNotEqual(seattle_coffee.item.description, "sweet")

    def test_request_item_to_warehouse(self):
        self.seattle_coffee.request_item(200)
        self.assertEqual(self.seattle_coffee.warehouse_inventory, 200)
        self.assertEqual(self.global_coffee.quantity,300)
        self.tacoma_coffee.request_item(300)
        self.assertEqual(self.tacoma_coffee.warehouse_inventory,300)
        self.assertEqual(self.global_coffee.quantity,0)

    def test_requesting_more_inventory_than_available_raises_exception(self):
        self.assertRaises(ValueError,self.seattle_coffee.request_item,600)

    def test_sell_item_from_warehouse(self):
        self.tacoma_coffee.request_item(50)
        self.tacoma_coffee.sell_item(50)
        self.assertEqual(self.tacoma_coffee.warehouse_inventory,0)
    
    def test_sell_more_inventory_than_available_raises_exception(self):
        self.assertRaises(ValueError,self.tacoma_coffee.sell_item,1)

    def test_return_item_to_global_inventory(self):
        self.tacoma_coffee.request_item(500)
        self.tacoma_coffee.return_item(100)
        self.assertEqual(self.tacoma_coffee.warehouse_inventory, 400)
        self.assertEqual(self.global_coffee.quantity,100)

    def test_returning_more_inventory_than_available_raises_exception(self):
        self.assertRaises(ValueError,self.seattle_coffee.return_item,1)