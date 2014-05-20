from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from wiki.urls import get_pattern as get_wiki_pattern
from django_notify.urls import get_pattern as get_notify_pattern

from .views import RootRouter

admin.autodiscover()


urlpatterns = i18n_patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^group/', include('workgroup.urls')),
	url(r'^project/', include('project.urls')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^wiki/', get_wiki_pattern()),
    url(r'^', include('cms.urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('social_auth.urls')),    
    url(r'^', include('accounts.urls')),  
    url(r'^notify/', get_notify_pattern()),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
