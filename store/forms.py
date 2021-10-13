from django.forms import ModelForm,Textarea
from django import forms
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','title','slug','description','price','color','in_stock','is_active','image']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows':4}),
        }

    def clean(self):
        data =self.cleaned_data
        title = data.get("title")
        slug = data.get("slug")

        if self.instance.id:
            if Product.objects.filter(title__icontains=title).exclude(id=self.instance.id).exists():
                self.add_error("title", f"{title} is already in use as a product name.")
            if Product.objects.filter(slug__icontains=slug).exclude(id=self.instance.id).exists():
                self.add_error("slug", f"{slug} is already in use as a slug name.")
        else:
            if Product.objects.filter(title__icontains=title).exists():
                self.add_error("title", f"{title} is already in use as a product name.")
            if Product.objects.filter(slug__icontains=slug).exists():
                self.add_error("slug", f"{slug} is already in use as a slug name.")
        return data
