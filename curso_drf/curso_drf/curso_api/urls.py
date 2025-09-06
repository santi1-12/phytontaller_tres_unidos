from django.contrib import admin
from django.urls import path, include
from .views import home
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Curso API",
        default_version="v1",
        description="Documentación de la API del curso (categorías, marcas y productos).",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', home, name='home'),  # 👈 Página de bienvenida
    path('admin/', admin.site.urls),
    path('api/catalogo/', include('catalogo.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
