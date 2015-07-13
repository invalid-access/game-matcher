from django.conf.urls import patterns, include, url
from django.contrib import admin

import matcher
from matcher import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game_matcher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^matcher/', include(matcher.urls)),
)
