from django.conf.urls import patterns, include, url

from .views import ProjectListView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ProjectListView.as_view(), name='project-list'),                       
)
