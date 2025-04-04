from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *
from .models import *

# Create your views here.
@api_view()
def index(request):
    return render(request, 'index.html', status=status.HTTP_200_OK)

class MenuItemView(generics.ListCreateAPIView):
    '''
    Handles POST and GET method calls
    '''
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Handles GET, PUT, and DELETE method calls for a single menu item
    '''
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 