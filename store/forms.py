from django import forms

# iterable
SHORT_CHOICES = (
    ("-created_date", "New First"),
    ("price", "price Low-High"),
    ("-price", "price High-Low"),

)


# creating a form
class ShortForm(forms.Form):
    short_field = forms.ChoiceField(label='Sort By', widget=forms.Select(attrs={'onchange': 'submit();'}), choices=SHORT_CHOICES)
