from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^index/$', 'webshare.views.index'),
    url(r'^about/$', 'webshare.views.about'),
    url(r'^asociaciones/$', 'webshare.views.asociaciones'),
    url(r'^investigadores/$', 'webshare.views.investigadores'),
    url(r'^empresa/$', 'webshare.views.empresa'),
    url(r'^ingenieros/$', 'webshare.views.ingenieros')
) 
