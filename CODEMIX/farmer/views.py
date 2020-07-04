from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import addCrop
from django.core.files.storage import FileSystemStorage
from .forms import addCropForm

# Create your views here.
def farmerlogin(request):
    if request.method=='POST':
        mobile_number=request.POST['mobile_number']
        password=request.POST['password']

        user=auth.authenticate(username=mobile_number,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('farmerhome')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('farmerlogin')

        
    else:
        return render(request,'farmerlogin.html')
def farmer(request):
    if request.method=='POST':
        full_name=request.POST['first_name']
        mobile_number=request.POST['mobile_number']
        aadhar=request.POST['aadhar']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=User.objects.create_user(first_name=full_name,last_name=aadhar,username=mobile_number,password=password1)
            user.save()
            return redirect('farmerlogin')
    
        else:
            messages.info(request, 'Password not matching')
            return redirect('farmer')
        return redirect('/')
    else:
        return render(request,'farmer.html')


def farmerlogout(request):
    auth.logout(request)
    return redirect('/')


def farmerhome(request):
    return render(request, 'farmerHome.html')        

def home(request):
    return render(request, 'farmerHome.html')     

def addPost(request):
    if request.method == 'POST':
        form = addCropForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seePost')
    else:        
        form = addCropForm()
    return render(request,'addPost.html', {
        'form': form
    })



def seePost(request):
    newCrop = addCrop.objects.all()
    return render(request,'posts.html',{
        'newCrop':newCrop
    })
