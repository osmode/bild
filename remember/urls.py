from django.conf.urls import patterns, url
from remember import views

urlpatterns=patterns('',
	url(r'^$',views.remember_bonescans,name='remember_bonescans')
	)
