from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('items/', views.MenuItemView.as_view(), name='items'),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]
