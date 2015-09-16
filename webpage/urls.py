from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', PrincipalListView.as_view(), name='principal.list.view'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^principal/(?P<pk>\d+)/$', PrincipalDetailView.as_view(), name='principal.detail.view'),
    url(r'^principal/add/$', PrincipalAddView.as_view(), name='principal.add.view'),
    url(r'^user/(?P<user_id>\d+)/site/(?P<site_id>\d+)/$', SiteDetailView.as_view(), name='site.detail.view'),
]
