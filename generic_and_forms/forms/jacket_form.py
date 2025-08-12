from django import forms

from generic_and_forms.models import Jacket


class JacketForm(forms.ModelForm):
    class Meta:
        model = Jacket
        fields = ['brand', 'color']  # вручну вказуємо поля
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
        }