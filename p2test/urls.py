"""from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('petpal.urls')),
    path('', include('accounts.urls')),
    path('', include('comments.urls')),
    path('', include('listings.urls')),
    path('',include('applications.urls')),
    path('', include('notifications.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
] + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view( openapi.Info( title="Pets API", default_version='1.0.0', description="API documentation of app" ), public=True )

urlpatterns = [
                  path('', include('accounts.urls')),
                  path('', include('comments.urls')),
                  path('', include('listings.urls')),
                  path('',include('applications.urls')),
                  path('', include('notifications.urls')),
                  path('admin/', admin.site.urls),
                  path('api/', include('api.urls')),
                  path('', include([path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")])) ] + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
