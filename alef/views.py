from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('this is the home page')
    return render(request,'homepage.html')

def contact(request):
    #return HttpResponse('this is the home page')
    return render(request,'contact.html')


def about(request):
    #return HttpResponse('this is the home page')
    return render(request,'about.html')