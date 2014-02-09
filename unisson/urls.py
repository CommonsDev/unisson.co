from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from .views import RootRouter

admin.autodiscover()

urlpatterns = i18n_patterns('',
	url(r'^$', RootRouter.as_view(), name='root'),
    url(r'^home$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('zinnia.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('social_auth.urls')),    
    url(r'^', include('accounts.urls')),  
)

urlpatterns += i18n_patterns('',
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
