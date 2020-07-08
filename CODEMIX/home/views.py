from django.shortcuts import render
from django.http import HttpResponse
from .models import Crop
# Create your views here.

def home(request):
    return render(request, 'home.html')

def price(request):
    crop = Crop.objects.all()

    return render(request, 'price.html',{'crop':crop})

def about(request):
    return render(request, 'about.html')    