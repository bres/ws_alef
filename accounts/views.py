from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.


def signup_view(request):
    if request.method =="POST" :
        account_form= UserCreationForm(request.POST)
        if account_form.is_valid():
            account_form.save()
            #log the user in_stock
            user = account_form.save()
            login(request,user)
            return redirect("store:all_products")
    else:
        account_form = UserCreationForm()
    return render(request,'accounts/signup.html',{'account_form':account_form}) 


def login_view(request):
    if request.method == 'POST':
        account_form = AuthenticationForm(data=request.POST)
        if account_form.is_valid():
             #log the user in_stock
            user = account_form.get_user()
            login(request,user)
            return redirect("store:all_products")
    else:
        account_form = AuthenticationForm()
    return render(request,'accounts/login.html',{'account_form':account_form}) 


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')     