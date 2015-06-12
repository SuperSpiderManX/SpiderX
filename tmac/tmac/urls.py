from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tmac.views.home', name='home'),
    # url(r'^tmac/', include('tmac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$','blog.views.index'),
    url(r'^blog/index1/$','blog.views.index1'),
    url(r'^blog/index2/$','blog.views.index2'),
    url(r'^blog/index3/$','blog.views.index3'),
    url(r'^blog/register/$','blog.views.register'),
	url(r'^online/', include('online.urls')),
)
