from django.conf.urls import patterns, url
from xdetect import views

urlpatterns=patterns('',
	url(r'^$',views.xdetect,name='xdetect'),
	)

