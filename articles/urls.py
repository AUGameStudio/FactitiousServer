from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^id/A(?P<article_id>[0-9]+)/$', views.article_json),
	url(r'^(?P<article_id>[0-9]+)/$', views.article_json),
	url(r'^list/$', views.all_articles),
]