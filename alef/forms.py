
from django import forms

class ContactForm(forms.Form):
    fullname =forms.CharField()
    email    =forms.EmailField()
    content  =forms.CharField(widget=forms.Textarea(attrs={'rows':5}))


    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("email must be gmail")
        return email