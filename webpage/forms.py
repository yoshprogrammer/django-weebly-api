from django import forms

from .models import Principal


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Principal
        fields = [
            'email',
        ]


class PrincipalAddForm(forms.ModelForm):
    class Meta:
        model = Principal
        fields = [
            'id',
        ]
