from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
# email verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

#Create your views here.

# def signup_view(request):
#     if request.method =="POST" :
#         account_form= UserCreationForm(request.POST)
#         if account_form.is_valid():
#             account_form.save()
#             user = account_form.save() # i do not need get because user is inside on the form
#             login(request,user)   #log the user in
#             return redirect("home")
#     else: #if it is a get request
#         account_form = UserCreationForm() # creating a fresh blank form
#     return render(request,'accounts/signup.html',{'account_form':account_form})
#
# def login_view(request):
#     if request.method == 'POST':
#         account_form = AuthenticationForm(data=request.POST)
#         if account_form.is_valid():
#             user = account_form.get_user()
#             login(request,user)  #log the user in
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect("home")
#     else: #if it is a get request
#         account_form = AuthenticationForm()
#     return render(request,'accounts/login.html',{'account_form':account_form})
#
#
# def logout_view(request):
#     if request.method == 'POST':
#         logout(request) #log out the user
#         return redirect('accounts:login')
#     return render(request,'accounts/logout.html')


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            username=email.split("@")[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.phone_number=phone_number
            user.save()


            #user activation
            current_site=get_current_site(request)
            mail_subject='Please acativate your account'
            message     =render_to_string('accounts/account_verification.html', {
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),

            })
            to_email = email
            send_email= EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Look for the verification email in your inbox and click the link in that email. A confirmation message will appear in your web browser.')
            return redirect('accounts:register')
    else:
        form=RegistrationForm()
    context = {
            'form':form,
            }
    return render(request,'accounts/register.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user=auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request,'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials.')
            return redirect('accounts:login')



    return render(request,'accounts/login.html')

@login_required(login_url='accounts:login')
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


def activate(request):
    return
