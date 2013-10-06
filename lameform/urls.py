from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'lameform.views.root', name='lameform'),
    url(r'graph/$', 'lameform.views.graph', name='lameform'),
)
