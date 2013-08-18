from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from api import views

urlpatterns = patterns('snippets.views',
    url(r'^accounts/register/$', views.UserRegistrationAPIView.as_view(), name='api_accounts_register'),
    url(r'^accounts/login/$', obtain_auth_token, name='api_accounts_login'),
    
    url(r'^offers/create/$', views.CreateOfferAPIView.as_view(), name='api_offer_create'),
    url(r'^offers/cancel/$', views.CancelOfferAPIView.as_view(), name='api_offer_cancel'),
    url(r'^offers/accept/$', views.AcceptOfferAPIView.as_view(), name='api_offer_accept'),
    url(r'^offers/reject/$', views.RejectOfferAPIView.as_view(), name='api_offer_reject'),
    url(r'^offers/list/deal/$', views.DealOfferAPIView.as_view(), name='api_deal_offer_list'),
    url(r'^offers/list/user/$', views.UserOfferAPIView.as_view(), name='api_user_offer_list'),
    
    url(r'^deals/create/$', views.CreateDealAPIView.as_view(), name='api_deal_create'),
    url(r'^deals/list/$', views.ListDealAPIView.as_view(), name='api_deal_list'),
    url(r'^deals/list/user/$', views.UserDealAPIView.as_view(), name='api_user_deal_list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
