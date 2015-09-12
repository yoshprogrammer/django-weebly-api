from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, TemplateView

from .utils import *
from .forms import *


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    model = Principal
    fields = ['email']

    def form_valid(self, form):
        # get data
        my_data = {
            'email': form.data['email'],
            'test_mode': True,
            'language': 'en',
            }

        # send off to weebly for user_id
        resp = weebly_api('POST', my_data, 'user/')

        if (resp.status_code == 200):
            form.instance.user_id = resp.json()['user']['user_id']
            form.instance.test_mode = resp.json()['user']['test_mode']
            form.instance.language = resp.json()['user']['language']
            return super(SignUpView, self).form_valid(form)
        else:
            # fail. redirect with message
            #TODO: form.errors = resp.json()['error']['message']
            return redirect('signup')


class PrincipalDetailView(DetailView):
    model = Principal