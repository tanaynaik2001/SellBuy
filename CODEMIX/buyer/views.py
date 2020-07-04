from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import requests
import json
# Create your views here.


def buyerlogin(request):
    if request.method=='POST':
        buyerusername = request.POST['buyerusername']
        buyerpassword=request.POST['buyerpassword1']

        user=auth.authenticate(username=buyerusername,password=buyerpassword)

        if user is not None:
            auth.login(request,user)
            return redirect('buyerhome')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('buyerlogin')

        
    else:
        return render(request,'buyerlogin.html')


def buyer(request):
    if request.method == 'POST':
        buyerusername = request.POST['buyerusername']
        buyeremail = request.POST['buyeremail']
        buyerpassword1 = request.POST['buyerpassword1']
        buyerpassword2 = request.POST['buyerpassword2']

        if buyerpassword1 == buyerpassword2:
            if User.objects.filter(username=buyerusername).exists():
                messages.info(request, 'Username already taken')
                return redirect('buyer')
            elif User.objects.filter(email=buyeremail).exists():
                messages.info(request, 'Email already taken')
                return redirect('buyer')
            else:
                user = User.objects.create_user(
                    username=buyerusername, email=buyeremail, password=buyerpassword1)
                user.save()

                subject = 'Successful Registration'
                message = f'Welcome to SELLBUY , the website where Farmer meets direct Buyers'
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email, settings.EMAIL_HOST_USER]

                send_mail(subject, message, from_email,
                          to_list, fail_silently=True)
                return redirect('buyerlogin')
        else:
            messages.info(request, 'Password not matching')
            return redirect('buyer')
        return redirect('/')
    else:
        return render(request, 'buyer.html')


def buyerlogout(request):
    auth.logout(request)
    return redirect('/')


def buyerhome(request):
    return render(request, 'buyerhome.html')
