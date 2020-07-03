from django.urls import include, path
from . import views

urlpatterns = [
    path('buyer', views.buyer, name='buyer'),
    path('buyerlogin', views.buyerlogin, name='buyerlogin'),
    path('buyerlogout', views.buyerlogout, name='buyerlogout'),
    path('buyerhome', views.buyerhome, name='buyerhome')
]
