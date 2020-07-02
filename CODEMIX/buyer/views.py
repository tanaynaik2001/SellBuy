from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
import requests
import json
# Create your views here.
def buyerlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        
        user = auth.authenticate(username=username, password=password)
        clientKey=request.POST['g-recaptcha-response']
        secretKey='6LdqfawZAAAAAFEFKeb_87e1PEiYyf40RKRi9TPf'

        captchaData={
            'secret':secretKey,
            'response':clientKey
        }
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchaData)
        response=json.loads(r.text)
        verify=response['success']
        print(f'Your success is {verify}')

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('buyerlogin')
    return render(request,'buyerlogin.html')


def buyer(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('buyer')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('buyer')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()

                subject = 'Successful Registration'
                message = f'Welcome to SELLBUY , the website where Farmer meets direct Buyers'
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email, settings.EMAIL_HOST_USER]

                send_mail(subject, message, from_email,
                           to_list, fail_silently=True)
                return redirect('buyerlogin')
        else:
            messages.info(request,'Password not matching')
            return redirect('buyer')
        return redirect('/')
    else:
        return render(request,'buyer.html')