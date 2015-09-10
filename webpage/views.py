from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/'