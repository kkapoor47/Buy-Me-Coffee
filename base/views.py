from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
import stripe

stripe.api_key = "sk_test_51HbnDUJo0BoszpvU40hd8WMyaYDWABqt1CsjbjwHGEIiq3kAi3dIL8Rl9NKAsGEnQRmlqS2csaMkgodH9MjRuKmI00u4dsd6aH"


# Create your views here.

def index(request):
    return render(request,'index.html')

def charge(request):
    
    if request.method=='POST':
        print('Data:',request.POST)

        amount = int(request.POST['amount'])
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']

        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='inr',
            description='Donation',

        )


    return redirect(reverse('success',args=[amount]))


def successMsg(request,args):
    amount=args
    return render(request,'success.html',{'amount':amount})