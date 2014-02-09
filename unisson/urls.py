from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from .views import RootRouter

admin.autodiscover()


urlpatterns = i18n_patterns('',
    url(r'^blog/', include('zinnia.urls')),
    url(r'^', include('cms.urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('social_auth.urls')),    
    url(r'^', include('accounts.urls')),  
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
