from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.users, name='all-customers'),
    path('customer/<str:pk>', views.user, name="customer"),
    path('add-customer/', views.addUser, name='add-customer'),
    path('update-customer/<str:pk>', views.updateUser, name="update-customer"),
    path('delete-customer/<str:pk>', views.deleteUser, name="delete-customer"),    
]