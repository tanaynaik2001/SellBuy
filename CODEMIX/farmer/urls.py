from django.urls import path
from . import views

urlpatterns=[
    path('farmer',views.farmer,name='farmer'),
    path('farmerlogin',views.farmerlogin,name='farmerlogin'),
    path('home', views.home, name='home'),
]