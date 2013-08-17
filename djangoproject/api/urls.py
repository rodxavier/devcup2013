from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = patterns('snippets.views',
    url(r'^accounts/register/$', views.UserRegistrationAPIView.as_view(), name='api_accounts_register'),
    url(r'^accounts/login/$', 'rest_framework.authtoken.views.obtain_auth_token', name='api_accounts_login'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
