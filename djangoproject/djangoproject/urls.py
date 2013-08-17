from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from djangoproject.shortcuts import UrlBuilder

admin.autodiscover()

ub = UrlBuilder('djangoproject')

urlpatterns = patterns('djangoproject.views',
    ub.build('index'),
    ub.build('login'),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'djangoproject.views.home', name='home'),
    # url(r'^djangoproject/', include('djangoproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include('api.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
