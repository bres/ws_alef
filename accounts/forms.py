from django import forms
from .models import Account,UserProfile
from django.contrib import messages

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'last_name','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))


    class Meta:
        model= Account
        fields = ['first_name','last_name','phone_number','email','password']


    def clean(self):
        cleaned_data =super(RegistrationForm,self).clean()
        password= cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password !=confirm_password:

            raise forms.ValidationError({'password':
            ["Passwords does not match"]}
            )


class UserForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'last_name','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'phone_number','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

    





class UserProfileForm(forms.ModelForm):
    address=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'address','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    city=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'city','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    state=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'state','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    country=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'country','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    municipality=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'municipality','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    post_code=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'post_code','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput(attrs={
        'placeholder': 'profile_picture','class':'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-300 text-gray-900 rounded-t-md focus:outline-none focus:ring-gray-500 focus:border-gray-500 focus:z-10 sm:text-sm'
    }))

  
    class Meta:
        model = UserProfile
        fields = ('address', 'city', 'state', 'country','municipality','post_code', 'profile_picture')

   
