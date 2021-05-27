from django import forms

from coffee_shop.models import Bakery


class BakeryForm(forms.ModelForm):
    class Meta:
        model = Bakery
        fields = ['quantity']
