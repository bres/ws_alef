from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,ProductSearchForm
from store.models import Product
# Create your views here.

def home(request):
    #return HttpResponse('this is the home page')
    return render(request,'homepage.html')

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


def product_search(request):
    if request.method == 'POST':
        searched = request.POST.get('search')
        products=Product.objects.filter(title__icontains=searched)
        context = { 'searched':searched ,'products':products }
        return render(request, 'product_search.html', context)

    else:
        return render(request, 'product_search.html')
