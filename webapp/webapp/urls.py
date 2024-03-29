from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'REST.views.index'),
    
    url(r'^sentiments/$', 'REST.views.sentiments', name='sentiments'),
    url(r'^company/$', 'REST.views.company'),
    url(r'^company/new/$', 'REST.views.new_company'),
    
    url(r'^parse_yahoo/$', 'REST.views.parse_yahoo'),
    url(r'^upload_tasks/$', 'REST.views.upload_all_tasks'),

    url(r'^callback/$', 'REST.views.callback'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
