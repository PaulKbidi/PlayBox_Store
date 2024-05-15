from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nom'
    )
    firstname = forms.CharField(
        max_length=100,
        label='Prénom'
    )
    email = forms.EmailField(
        label='Email'
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Message'
    )
    
class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)