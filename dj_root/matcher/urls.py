from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<playgroup_id>[0-9]+)/$', views.match, name='match'),
    url(r'^match/(?P<playgroup_id>[0-9]+)/$', views.match, name='match'),

]