from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    path('home', views.index, name='home'),
    path('items/', views.MenuItemView.as_view(), name='items'),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]
