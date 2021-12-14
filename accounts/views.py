from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from .models import Account
from orders.models import Order
from django.contrib import messages,auth
# email verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from carts.views import _cart_id
from carts.models import Cart,CartItem 
import requests

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


            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(request, 'Thank you for registering with us. We have sent you a verification email to your email address [rathan.kumar@gmail.com]. Please verify it.')
            return redirect('/accounts/login/?command=verification&email='+email)

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
            try:
                cart=Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists =CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item=CartItem.objects.filter(cart=cart)
                    # getting the product varition by cart_id
                    product_variation=[]
                    for item in cart_item:
                        variation=item.variations.all()
                        product_variation.append(list(variation))

                    #get the cart items from user to access his product variations
                    cart_item=CartItem.objects.filter(user=user)
                    ex_var_list=[]
                    id=[]
                    for item in cart_item:
                        existing_variation=item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)

                    for pr in product_variation:
                        if pr in ex_var_list:
                            index=ex_var_list.index(pr)
                            item_id=id[index]
                            item=CartItem.objects.get(id=item_id)
                            item.quantity +=1
                            item.user=user
                            item.save()
                        else:
                            cart_item=CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request,'You are now logged in.')
            url= request.META.get('HTTP_REFERER')
            try:
                query =requests.utils.urlparse(url).query
                # print('query -->',query)
                #next=/cart/checkout
                params=dict(x.split('=') for x in query.split('&'))
                # print('params -->',params)
                if 'next' in params:
                    nextPage=params['next']
                    return redirect(nextPage)
            except:
                return redirect('accounts:dashboard')

        else:
            messages.error(request,'Invalid login credentials.')
            return redirect('accounts:login')



    return render(request,'accounts/login.html')

@login_required(login_url='accounts:login')
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist ):
        user=None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active  =True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('accounts:login')

    else:
        messages.error(request,'Invalid activation link')
        return redirect('accounts:register')

@login_required(login_url='login')
def dashboard(request):
    orders = Order.objects.order_by('created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    context={
        'orders_count':orders_count,
    }
    return render(request,'accounts/dashboard.html',context)


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__exact=email)
            #reset password with email
            current_site = get_current_site(request)
            mail_subject = 'Reset your password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request,'Password reset email has been sent to your email address')
            return redirect('accounts:login')
        else:
            messages.error(request,'Account does not exist')
            return redirect('accounts:forgotPassword')
    return render(request,'accounts/forgotPassword.html')    


def resetpassword_validate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist ):
        user=None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid']=uid
        messages.success(request, 'Please reset your password')
        return redirect('accounts:resetPassword')
    else:
        messages.error(request,'This link has been expired')
        return redirect('accounts:login')
            

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password =request.POST['confirm_password']

        if password == confirm_password:
            uid= request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Passowrd reset succeefull')
            return redirect('accounts:login')


        else:
            messages.error(request,'Passwords do not match!')
            return redirect('accounts:resetPassword')

    else: 
            
        return render(request,'accounts/resetPassword.html')


@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/my_orders.html', context)