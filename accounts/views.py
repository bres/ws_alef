from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def signup_view(request):
    if request.method =="POST" :
        account_form= UserCreationForm(request.POST)
        if account_form.is_valid():
            account_form.save()
            user = account_form.save() # i do not need get because user is inside on the form
            login(request,user)   #log the user in
            return redirect("home")
    else: #if it is a get request
        account_form = UserCreationForm() # creating a fresh blank form
    return render(request,'accounts/signup.html',{'account_form':account_form})

def login_view(request):
    if request.method == 'POST':
        account_form = AuthenticationForm(data=request.POST)
        if account_form.is_valid():
            user = account_form.get_user()
            login(request,user)  #log the user in
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("home")
    else: #if it is a get request
        account_form = AuthenticationForm()
    return render(request,'accounts/login.html',{'account_form':account_form})


def logout_view(request):
    if request.method == 'POST':
        logout(request) #log out the user
        return redirect('accounts:login')
    return render(request,'accounts/logout.html')
