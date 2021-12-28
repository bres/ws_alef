
from django import forms

class ContactForm(forms.Form):
    
    fullname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), required=True)

    

  

 
