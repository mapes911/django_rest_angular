from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from experiences import views


urlpatterns = format_suffix_patterns(patterns('',
    url(r'^$', views.api_root),
    url(r'^experiences/$',
        views.ExperienceList.as_view(),
        name='experience-list'),
    url(r'^experiences/(?P<pk>[0-9]+)/$',
        views.ExperienceDetail.as_view(),
        name='experience-detail'),
    url(r'^chapters/(?P<pk>[0-9]+)/$',
        views.ChapterDetail.as_view(),
        name='chapter-detail'),
))
