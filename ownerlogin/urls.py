from django.urls import path
from . import views

urlpatterns = [
    path("", views.ownerLogin, name='ownerlogin-ownerLogin'),

]
