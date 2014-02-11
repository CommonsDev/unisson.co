from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
                       
     url(r'^(?P<slug>[-\w]+)/$', views.GroupDetailView.as_view(), name='workgroup-detail'),
     url(r'^(?P<slug>[-\w]+)/members$', views.GroupMembersView.as_view(), name='workgroup-members'),
     url(r'^(?P<slug>[-\w]+)/archive$', views.GroupListArchiveView.as_view(), name='workgroup-list-archive'),

    # Subscriptions
     url(r'^(?P<workgroup_slug>[-\w]+)/subscribe/$', views.SubscribeView.as_view(), name='workgroup-subscribe'),
     url(r'^(?P<workgroup_slug>[-\w]+)/unsubscribe/$', views.UnsubscribeView.as_view(), name='workgroup-unsubscribe'),


)

