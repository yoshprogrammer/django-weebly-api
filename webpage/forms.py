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


class SiteAddForm(forms.Form):
    domain = forms.CharField(label='Domain name', max_length=255)