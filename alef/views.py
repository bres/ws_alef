from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from store.models import Product,Category
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.

def home(request):
    products = Product.objects.filter().order_by('-created_date')[0:4]
    context={
            'products': products,
 
    }
    return render(request,'homepage.html',context)

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                'message from'+' '+ fullname +' with email address '+ email , #subject
                     message, #message
                     email, #from email
                    [settings.EMAIL_HOST_USER], #to email
                    )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            form = ContactForm()
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def success(request):
    return render(request, "success.html")


def about(request):
    return render(request,'about.html')



def wholesale(request):
    return render(request,'wholesale.html')


def terms(request):
    return render(request,'terms.html')

def shipping(request):
    return render(request,'shipping.html')