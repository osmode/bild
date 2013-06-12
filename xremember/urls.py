from django.conf.urls import patterns, url
from xremember import views

urlpatterns=patterns('',
	url(r'^$',views.remember_image,name='remember_image'),
	)


