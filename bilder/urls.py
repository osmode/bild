from django.conf.urls import patterns, include, url
from views import flush

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bilder.views.home', name='home'),
    # url(r'^bilder/', include('bilder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #ex: /remember
    url(r'^remember/',include('remember.urls',namespace="remember")),
    url(r'^detect/',include('detect.urls',namespace="detect")),
    url(r'^xremember/',include('xremember.urls',namespace="xremember")),
    url(r'^xdetect/',include('xdetect.urls',namespace="xdetect")),
    url(r'^flush/', flush, name='flush'),

)
