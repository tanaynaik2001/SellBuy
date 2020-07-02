from django.urls import path
from . import views

urlpatterns=[
    path('',views.farmer,name='farmer'),
    path('farmerlogin',views.farmerlogin,name='farmerlogin')
]