from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.editMenu, name='ownerpages-editMenu'),
    path("signout/", views.signOut, name='ownerpage-signout'),
    path("inventory/", views.inventoryPage, name='ownerpage-inventory'),
    path("orders/", views.ordersPage, name='ownerpages-orders'),
    path("sales/", views.salesPage, name='ownerpages-sales')
]
