from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import addCrop
from django.core.files.storage import FileSystemStorage

# Create your views here.

def farmerlogin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        # aadhar = request.POST['aadhar']
        password=request.POST['password1']

        user = auth.authenticate(first_name=first_name,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Enter the correct password')
            return redirect('farmerlogin')
    else:
        return render(request,'farmerlogin.html')
def farmer(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        aadhar=request.POST['aadhar']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=aadhar,password=password1)
            user.save()
            return redirect('farmerlogin')
    
        else:
            messages.info(request, 'Password not matching')
            return redirect('farmer')
        return redirect('/')
    else:
        return render(request,'farmer.html')

def home(request):
    return render(request, 'farmerHome.html')     

def addPost(request):
    return render(request, 'addPost.html')

def addCropPost(request):
    if request.method == 'POST':  
        
        cropNew = addCrop()
        cropNew.addCropName = request.POST['crop_name']
        cropNew.addCropDescription = request.POST['crop_info']
        cropNew.addCropPrice = request.POST['price']

        cropNew.addCropImg = request.POST['photo_input']
        cropNew.save()

        return render(request,'farmerHome.html')

def seePost(request):
    newCrop = addCrop.objects.all()
    return render(request,'posts.html', {'newCrop': newCrop})
