from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.openapi import Info, Contact, License
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.utils.translation import gettext_lazy as _


admin.site.site_title = _("OOO DoodMall")
admin.site.site_header = _("DoodMall Administration")
admin.site.index_title = _("Admin Panel")

schema_view = get_schema_view(
    Info(
        title="DoodMall API",
        default_version='v1',
        description=_("API for DoodMall"),
        terms_of_service="https://www.google.com/policies/terms/",
        contact=Contact(email="contact@snippets.local"),
        license=License(name="NO License"),
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = i18n_patterns(
    # Default
    path('admin/', admin.site.urls, name='admin'),
    # Custom
    path('api/', include('users.urls')),
    # path('api/', include('products.urls')),
    # Debug tool
    path('__debug__/', include('debug_toolbar.urls')),
    # Swagger/ API Documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("i18n/", include("django.conf.urls.i18n")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('translations/', include('rosetta.urls'))
    ]
