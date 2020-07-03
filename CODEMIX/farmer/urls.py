from django.urls import path
from . import views

urlpatterns=[
    path('farmer',views.farmer,name='farmer'),
    path('farmerlogin',views.farmerlogin,name='farmerlogin'),
    path('home', views.home, name='home'),
    path('addPost', views.addPost, name='addPost'),
    path('addCropPost', views.addCropPost, name='addCropPost'),
    path('seePost', views.seePost, name='seePost'),
]