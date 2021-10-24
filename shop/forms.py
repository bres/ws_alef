from django.forms import ModelForm,Textarea
from django import forms
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','slug','image','description','marked_price','selling_price','available']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows':4}),
        }

    def clean(self):
        data =self.cleaned_data
        name = data.get("name")
        slug = data.get("slug")

        if self.instance.id:
            if Product.objects.filter(name__icontains=name).exclude(id=self.instance.id).exists():
                self.add_error("name", f"{name} is already in use as a product name.")
            if Product.objects.filter(slug__icontains=slug).exclude(id=self.instance.id).exists():
                self.add_error("slug", f"{slug} is already in use as a slug name.")
        else:
            if Product.objects.filter(name__icontains=name).exists():
                self.add_error("title", f"{name} is already in use as a product name.")
            if Product.objects.filter(slug__icontains=slug).exists():
                self.add_error("slug", f"{slug} is already in use as a slug name.")
        return data
