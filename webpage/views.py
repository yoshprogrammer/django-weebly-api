from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404

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
        resp = weebly_api('POST', 'user/', my_data)

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

    def get_context_data(self, **kwargs):
        context = super(PrincipalDetailView, self).get_context_data(**kwargs)

        #fetch sites from weebly
        principal = get_object_or_404(Principal, pk=self.kwargs['pk'])
        user_id = principal.user_id
        my_url = 'user/' + str(user_id) + '/site'
        resp = weebly_api('GET', 'my_url')

        if (resp.status_code == 200):


        else:
            #TODO need error message
            return redirect('principal.list.view')

        return context



class PrincipalListView(ListView):
    model = Principal