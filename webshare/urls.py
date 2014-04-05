from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^home/$', 'webshare.views.index'),
    url(r'^home/about/$', 'webshare.views.master')
) 
