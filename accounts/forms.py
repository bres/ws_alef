from django import forms
from .models import Account
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
