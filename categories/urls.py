#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from taxonomy.contrib.category_tree.models import Category

urlpatterns = patterns('',
    url(r'^list/$', ListView.as_view(model = Category), name='categories_list'),

)