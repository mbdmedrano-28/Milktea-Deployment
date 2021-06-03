from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginPage, name='loginsignup-login'),
    path("signup/", views.signupPage, name='loginsignup-signup'),
    path("about/", views.aboutPage, name='loginsignup-about')
]
