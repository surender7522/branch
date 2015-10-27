__author__ = 'surender'
from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns('',
(r'^$', 'branch_change.views.post_list'),
(r'^login/$', 'branch_change.views.lin'),
(r'^create/$', 'branch_change.views.create_user'),
(r'^logout/$', 'branch_change.views.lout'),
(r'^(?P<poll_id>\d+)/$', 'branch_change.views.details'),
(r'^(?P<poll_id>\d+)/results/$', 'branch_change.views.results'),
(r'^(?P<poll_id>\d+)/vote/$', 'branch_change.views.vote'))
