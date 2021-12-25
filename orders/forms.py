from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    DELIVERY = (
        ('Shipping', 'Shipping'),
        ('Collect From Store', 'Collect From Store'),
    )
    delivery=forms.ChoiceField(choices=DELIVERY,widget=forms.RadioSelect)
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'municipality', 'country','post_code', 'state', 'city', 'order_note','delivery']
