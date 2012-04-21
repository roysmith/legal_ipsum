from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='legal_ipsum/home.html'), name='home'),
    url(r'^text$', 'legal_ipsum.views.text'),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
