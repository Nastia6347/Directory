__author__ = 'user'
from django.conf.urls import patterns, url

from directory import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<category_id>\d+)/$', views.category, name='category'),
                       )