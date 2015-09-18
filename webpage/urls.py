from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^$', UserListView.as_view(), name='user.list'),
    url(r'^user/add/$', UserAddView.as_view(), name='user.add'),
    url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user.detail'),
    url(r'^user/(?P<user_id>\d+)/site/add/$', SiteAddView.as_view(), name='site.add'),
    url(r'^user/(?P<user_id>\d+)/site/(?P<site_id>\d+)/$', SiteDetailView.as_view(), name='site.detail'),
    url(r'^user/(?P<user_id>\d+)/site/(?P<site_id>\d+)/loginlink/$', SiteLoginLinkView.as_view(), name='site.login.link')
]
