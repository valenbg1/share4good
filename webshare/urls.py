from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^index/$', 'webshare.views.index'),
    url(r'^about/$', 'webshare.views.master')
) 
