from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^$', PrincipalListView.as_view(), name='principal.list'),
    url(r'^principal/add/$', PrincipalAddView.as_view(), name='principal.add'),
    url(r'^principal/(?P<pk>\d+)/$', PrincipalDetailView.as_view(), name='principal.detail'),
    url(r'^user/(?P<user_id>\d+)/site/add/$', SiteAddView.as_view(), name='site.add'),
    url(r'^user/(?P<user_id>\d+)/site/(?P<site_id>\d+)/$', SiteDetailView.as_view(), name='site.detail'),
    url(r'^user/(?P<user_id>\d+)/site/(?P<site_id>\d+)/loginlink/$', SiteLoginLinkView.as_view(), name='site.login.link')
]
