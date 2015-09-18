from django import forms

from .models import *


class SignUpForm(forms.ModelForm):
    class Meta:
        model = WeeblyUser
        fields = [
            'email',
        ]


class PrincipalAddForm(forms.ModelForm):
    class Meta:
        model = WeeblyUser
        fields = [
            'id',
        ]


class SiteAddForm(forms.Form):
    domain = forms.CharField(label='Domain name', max_length=255)