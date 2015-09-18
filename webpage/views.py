from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, FormView, ListView, TemplateView
from django.core.urlresolvers import reverse
from django.conf import settings

from weebly import WeeblyClient

from .utils import *
from .forms import *

wclient = WeeblyClient(api_key=settings.WEEBLY_API_KEY, api_secret=settings.WEEBLY_API_SECRET )


# Create your views here.

class SignUpView(CreateView):
    model = WeeblyUser
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


class UserListView(ListView):
    model = WeeblyUser


class UserAddView(CreateView):
    model = WeeblyUser
    fields = ['id']
    success_url = 'user.list'


class UserDetailView(DetailView):
    model = WeeblyUser

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)

        #fetch sites from weebly
        user = get_object_or_404(WeeblyUser, pk=self.kwargs['pk'])
        my_url = 'user/' + str(user.id) + '/site'
        resp = wclient.get(my_url)

        if (resp.status_code == 200):
            sites = resp.json()['sites']
            if sites == None:
                context['sites'] = []
            else:
                context['sites'] = [x['site_id'] for x in sites]
        else:
            #TODO need error message
            return HttpResponseRedirect(reverse('user.list'))

        return context


class SiteAddView(FormView):
    template_name = 'webpage/site_add.html'
    form_class = SiteAddForm

    def form_valid(self, form):
        user_id = self.kwargs['user_id']
        domain = form.cleaned_data #leave it as json

        # first check if valid hostname
        if is_valid_hostname(domain['domain']):
            my_url = 'user/' + self.kwargs['user_id'] + '/site'
            my_data = domain
            resp = wclient.post(my_url, my_data)
            if resp.status_code != 200:
                # error msg
                return HttpResponseRedirect('user.detail', kwargs={'pk':user_id})

        return super(SiteAddView,self).form_valid(form)

    def get_success_url(self):
        user_id = self.kwargs['user_id']
        return reverse('user.detail', kwargs={'pk':user_id})


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
            return HttpResponseRedirect(reverse('user.detail', kwargs={'pk':user_id}))

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
            return HttpResponseRedirect(reverse('user.detail', kwargs={'pk':user_id}))

        return context
