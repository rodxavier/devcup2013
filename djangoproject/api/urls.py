from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from api import views

urlpatterns = patterns('snippets.views',
    url(r'^accounts/register/$', views.UserRegistrationAPIView.as_view(), name='api_accounts_register'),
    url(r'^accounts/login/$', obtain_auth_token, name='api_accounts_login'),
    
    url(r'^offers/create/$', views.CreateOfferAPIView.as_view(), name='api_offer_create'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
