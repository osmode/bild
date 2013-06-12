from django.conf.urls import patterns, url
from detect import views

urlpatterns=patterns('',
	url(r'^$',views.detect,name='detect')
	)

