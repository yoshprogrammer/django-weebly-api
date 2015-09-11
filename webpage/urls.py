from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index' ),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^principal/(?<pk>\d+)/$', PrincipalDetailView.as_view(), name='principal.detail.view')

]
