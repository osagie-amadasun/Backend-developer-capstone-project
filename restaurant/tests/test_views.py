from django.test import TestCase
from ..models import Menu
from ..serializers import MenuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Pizza", Price=120, Inventory=50)
        Menu.objects.create(Title="Pasta", Price=90, Inventory=75)
    
    def test_getall(self):
        # Retrieve all Menu objects
        menu_items = Menu.objects.all()
        
        # Serialize the data
        serializer = MenuSerializer(menu_items, many=True)
        
        # Get the response from the API endpoint
        url = reverse('items')  # Assuming you have a URL named 'menu-list'
        response = self.client.get(url)
        
        # Assert that the serialized data equals the response
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)



