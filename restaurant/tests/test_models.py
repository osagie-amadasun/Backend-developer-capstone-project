# tests/test_models.py
from django.test import TestCase
from ..models import Menu, Booking

class MenuTest(TestCase):
    def test_create_menu_item(self):
        """Test that a new Menu item can be created and its string representation is correct."""
        item = Menu.objects.create(Title="Pizza", Price=12.9, Inventory=50)
        self.assertEqual(str(item), "Pizza : 12.9")

    def test_another_menu_item(self):
        """Another test case for the Menu model."""
        item = Menu.objects.create(Title="Salad", Price=8.5, Inventory=100)
        self.assertEqual(str(item), "Salad : 8.5")

