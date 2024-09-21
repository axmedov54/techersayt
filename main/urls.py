from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/', include('api.urls')),
    # # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('account', include('allauth.urls')),
    # # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)