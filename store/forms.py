from django.forms import ModelForm,Textarea
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','title','slug','description','price','color','in_stock','is_active','image','created_by']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows':4}),
        }
