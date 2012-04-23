from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', 'legal_ipsum.views.home'),
    url(r'^about$', 'legal_ipsum.views.about'),
    url(r'^credits$', 'legal_ipsum.views.credits'),
)
