from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

urlpatterns = patterns('',
        url(r'^current-senators/$', 'public_views.datapages.views.current_senators'),
)