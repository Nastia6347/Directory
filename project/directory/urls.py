__author__ = 'user'
from django.conf.urls import patterns, url
from directory import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<slug>[-\w]+)/$', views.category, name='category'),
                       )