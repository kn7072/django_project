from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name='article'),
    url(r'^assets/$', 'blog.views.assets', name='assets'),
    url(r'^assets/my_form/$', 'blog.views.my_form', name='my_form'),
)
