from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView

from .forms import *


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    model = Principal
    fields = ['email']
    
    def form_valid(self, form):
        user_id
        test_mode = True
        language = 'en'

        return super(SignUpView, self).form_valid()



class PrincipalDetailView(DetailView):
    model = Principal