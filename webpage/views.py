from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404
from django.conf import settings

from weebly import WeeblyClient

from .forms import *

wclient = WeeblyClient(api_key=settings.WEEBLY_API_KEY, api_secret=settings.WEEBLY_API_SECRET )


# Create your views here.

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
        resp = wclient.post('user/', my_data)

        if (resp.status_code == 200):
            form.instance.user_id = resp.json()['user']['user_id']
            form.instance.test_mode = resp.json()['user']['test_mode']
            form.instance.language = resp.json()['user']['language']
            return super(SignUpView, self).form_valid(form)
        else:
            # fail. redirect with message
            #TODO: form.errors = resp.json()['error']['message']
            return redirect('signup')


class PrincipalAddView(CreateView):
    model = Principal
    fields = ['id']
    success_url = 'principal.list.view'



class PrincipalDetailView(DetailView):
    model = Principal

    def get_context_data(self, **kwargs):
        context = super(PrincipalDetailView, self).get_context_data(**kwargs)

        #fetch sites from weebly
        principal = get_object_or_404(Principal, pk=self.kwargs['pk'])
        my_url = 'user/' + str(principal.id) + '/site'
        resp = wclient.get(my_url)

        if (resp.status_code == 200):
            sites = resp.json()['sites']
            if sites == None:
                context['sites'] = []
            else:
                context['sites'] = [x['site_id'] for x in sites]
        else:
            #TODO need error message
            return redirect('principal.list.view')

        return context



class PrincipalListView(ListView):
    model = Principal


class SiteDetailView(TemplateView):
    template_name = 'webpage/site_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SiteDetailView, self).get_context_data(**kwargs)

        user_id = self.kwargs['user_id']
        site_id = self.kwargs['site_id']
        my_url = 'user/' + str(user_id) + '/site/' + str(site_id)

        resp = wclient.get(my_url)

        if (resp.status_code == 200):
            context['site_data'] = resp.json()['site']
        else:
            return redirect('pricipal.detail.view', kwargs={'user_id':user_id})

        return context


class SiteLoginLinkView(TemplateView):
    template_name = 'webpage/site_loginlink.html'

    def get_context_data(self, **kwargs):
        context = super(SiteLoginLinkView, self).get_context_data(**kwargs)

        user_id = self.kwargs['user_id']
        site_id = self.kwargs['site_id']
        my_url = 'user/' + str(user_id) + '/site/' + str(site_id) + '/loginLink'

        resp = wclient.get(my_url)

        if (resp.status_code == 200):
            context['loginLink'] = resp.json()['link']
        else:
            return redirect('principal.detail.view', kwargs={'user_id':user_id})

        return context
