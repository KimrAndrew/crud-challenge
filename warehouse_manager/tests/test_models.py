from django.test import TestCase
from warehouse_manager.models.Warehouse import Warehouse
from warehouse_manager.models.WarehouseItem import WarehouseItem
from inventory_manager.models.BaseProduct import BaseProduct

class WarehouseTestCase(TestCase):
    def test_instantiate_warehouse(self):
        expected_data = {"location":"Seattle"}
        warehouse = Warehouse.objects.create(location="Seattle")
        self.assertEqual(warehouse.location, expected_data["location"])

class WarehouseItemTestCase(TestCase):

    def setUp(self) -> None:
        # Create Product
        global_coffee = BaseProduct(name="coffee", description="bitter", price = 6)
        global_coffee.save()

        # Create Warehouses
        seattle = Warehouse(location = "Seattle")
        seattle.save()
        tacoma = Warehouse(location="Tacoma")
        tacoma.save()
        bellevue = Warehouse(location="Bellevue")
        bellevue.save()

        # Create Inventory Items using Product and Warehouses
        seattle_coffee = WarehouseItem(warehouse=seattle, item=global_coffee, quantity=200)
        seattle_coffee.save()
        tacoma_coffee = WarehouseItem(warehouse=tacoma, item=global_coffee, quantity=300)
        tacoma_coffee.save()
        bellevue_coffee = WarehouseItem(warehouse=bellevue, item=global_coffee, quantity=400)
        bellevue_coffee.save()
        

    def test_instantiate_WarehouseItem(self):
        seattle = Warehouse.objects.get(location="Seattle")
        coffee = BaseProduct.objects.get(name='coffee')
        seattle_coffee = WarehouseItem(warehouse=seattle, item=coffee, quantity=0)

        self.assertEqual(seattle_coffee.warehouse, seattle)
        self.assertEqual(seattle_coffee.item, coffee)
        self.assertEqual(seattle_coffee.quantity, 0)
        self.assertNotEqual(seattle_coffee.item.description, "sweet")

    def test_allocated_products(self):
        coffee_inventory = WarehouseItem.items.allocated_products(BaseProduct.objects.get(name='coffee'))
        print(coffee_inventory)
        self.assertTrue(coffee_inventory.filter(warehouse__location="Seattle").exists())
        self.assertTrue(coffee_inventory.filter(warehouse__location="Tacoma").exists())
        self.assertTrue(coffee_inventory.filter(warehouse__location="Bellevue").exists())

    # def test_request_item_to_warehouse(self):
    #     self.seattle_coffee.request_item(200)
    #     self.assertEqual(self.seattle_coffee.warehouse_inventory, 200)
    #     self.assertEqual(self.global_coffee.quantity,300)
    #     self.tacoma_coffee.request_item(300)
    #     self.assertEqual(self.tacoma_coffee.warehouse_inventory,300)
    #     self.assertEqual(self.global_coffee.quantity,0)

    # def test_requesting_more_inventory_than_available_raises_exception(self):
    #     self.assertRaises(ValueError,self.seattle_coffee.request_item,600)

    # def test_sell_item_from_warehouse(self):
    #     self.tacoma_coffee.request_item(50)
    #     self.tacoma_coffee.sell_item(50)
    #     self.assertEqual(self.tacoma_coffee.warehouse_inventory,0)
    
    # def test_sell_more_inventory_than_available_raises_exception(self):
    #     self.assertRaises(ValueError,self.tacoma_coffee.sell_item,1)

    # def test_return_item_to_global_inventory(self):
    #     self.tacoma_coffee.request_item(500)
    #     self.tacoma_coffee.return_item(100)
    #     self.assertEqual(self.tacoma_coffee.warehouse_inventory, 400)
    #     self.assertEqual(self.global_coffee.quantity,100)

    # def test_returning_more_inventory_than_available_raises_exception(self):
    #     self.assertRaises(ValueError,self.seattle_coffee.return_item,1)