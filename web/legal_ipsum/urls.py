from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='legal_ipsum/home.html'), name='home'),
    url(r'^text$', 'legal_ipsum.views.text'),
    url(r'^about$', TemplateView.as_view(template_name='legal_ipsum/about.html')),
)
