from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', 'legal_ipsum.views.home'),
    url(r'^about$',
        TemplateView.as_view(template_name='legal_ipsum/about.html'),
        {'extra_context': {"pagename": "about"}}),
    url(r'^credits$',
        TemplateView.as_view(template_name='legal_ipsum/credits.html'),
        {'extra_context': {"pagename": "credits"}}),
)
