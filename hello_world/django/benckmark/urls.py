# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'benckmark.views.benchmark', name='home'),
    # url(r'^$', 'benckmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
]
