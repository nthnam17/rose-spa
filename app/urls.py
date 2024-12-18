from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('service/', views.service, name="service"),
    path('register/', views.register, name="register"),
]