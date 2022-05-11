from django.test import TestCase
from .models.Manufacturer import Manufacturer

# Create your tests here.
class ManufacturerTestCase(TestCase):
    def test_create_manufacturer(self):
        gucci = Manufacturer.objects.create(name='Gucci')
        nike = Manufacturer.objects.create(name='Nike')
        self.assertEquals(gucci.name, 'Gucci')
        self.assertEqual(nike.name, 'Nike')

