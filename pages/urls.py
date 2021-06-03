from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.homePage, name='pages-home'),
    path("menu/", views.menuPage, name='pages-menu'),
    path("myCart/", views.cartPage, name='pages-cart'),
    path("myOrder/", views.orderPage, name='pages-order'),
    path("checkout/", views.infoPage, name='pages-info'),
    path("menu/sizes/", views.sizePage, name='pages-size'),
    path("myAccount/", views.accountPage, name='pages-account'),
    path("myAccount/settings/", views.settingsPage, name='pages-settings'),
    path("signout/", views.signOut, name='signout')
]
