from django.conf.urls import patterns, url
from bank import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^not_registered/$',views.not_registered,name='not_registered'),
	url(r'^search/$',views.search,name='search'),
	url(r'^count/$', views.blood_count, name='blood_counts'),
	url(r'^city/(?P<place>\w+)/$', views.city, name='place'),
	url(r'^navigate/(?P<user>\w+)/$', views.navigate, name='navigate'),
	]
