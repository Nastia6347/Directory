__author__ = 'user'
from django.conf.urls import patterns, url
from directory.views import index, search, category

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^search/$', search, name='search'),
                       url(r'(?P<slug>[-\w]+)/$', category, name='category'),
                       )