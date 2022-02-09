from django import forms

# iterable
SHORT_CHOICES = (
    ("-created_date", "New first "),
    ("price", "Price low first "),
    ("-price", "Price high first "),
    ("discount_percentage", "Discounts "),

)


# creating a form
class ShortForm(forms.Form):
    short_field = forms.ChoiceField(label='', widget=forms.Select(attrs={'onchange': 'submit();'}),
                                    choices=SHORT_CHOICES)
