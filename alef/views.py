from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from store.models import Product,Category
# Create your views here.

def home(request):
    #return HttpResponse('this is the home page')
    products = Product.objects.filter().order_by('-created_date')[0:4]
    context={
            'products': products,
 
    }
    return render(request,'homepage.html',context)

def contact(request):
    contact_form=ContactForm(request.POST or None)
    context ={
           "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'contact.html',context)


def about(request):
    #return HttpResponse('this is the home page')
    return render(request,'about.html')
