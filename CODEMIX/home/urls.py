from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('price', views.price, name='price'),
    path('about', views.about, name='about'),
]
