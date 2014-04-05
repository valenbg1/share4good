from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^index/$', 'webshare.views.index'),
    url(r'^about/$', 'webshare.views.about'),
    url(r'^asociaciones/$', 'webshare.views.asociaciones'),
    url(r'^investigadores/$', 'webshare.views.investigadores'),
) 
