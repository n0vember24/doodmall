from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.openapi import Info, Contact, License
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    Info(
        title="DoodMall API",
        default_version='v1',
        description="API for DoodMall",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=Contact(email="contact@snippets.local"),
        license=License(name="NO License"),
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    # Default
    path('admin/', admin.site.urls),
    # Debug tool
    path('__debug__/', include('debug_toolbar.urls')),
    # Swagger/ API Documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
