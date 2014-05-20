from django.conf.urls import patterns, include, url
import views
from .views import ProjectListView, PracticeListView, UsageListView, ProjectStartView

urlpatterns = patterns('',
    # Examples:
    url(r'^add/$', views.ProjectStartView.as_view(success_url='/project/'), name='project_sheet-start'),
    url(r'^(?P<slug>[-\w]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^$', ProjectListView.as_view(), name='project-list'),                       
    url(r'^practice$', PracticeListView.as_view(), name='practice-list'),          
    url(r'^usage$', UsageListView.as_view(), name='usage-list'),                      
)
