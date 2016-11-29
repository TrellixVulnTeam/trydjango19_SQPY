from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
# call url: posts:name
	url(r'^$', views.posts_list, name="list"),
    url(r'^create/$', views.posts_create),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name = "detail"),
    url(r'^(?P<id>\d+)/edit/$', views.posts_update, name = "update"),
    url(r'^(?P<id>\d+)/delete/$', views.posts_delete),

]