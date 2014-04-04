from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^home/$', 'webshare.views.home'),
) 