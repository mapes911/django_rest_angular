from django.conf.urls import patterns, include
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('experiences.urls'))
)
