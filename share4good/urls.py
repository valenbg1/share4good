from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
from userprofile.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'share4good.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^webshare/', include( 'webshare.urls' )),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register_user/$', register_user),
    url(r'^register_org/$', register_org),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
)
