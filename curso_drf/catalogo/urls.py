from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    CategoriaDetailView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    MarcaDetailView,
)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='productos-list'),
    path('productos/<int:id>/', ProductoDetailView.as_view(), name='producto-detalle'),
    path('productos/crear/', ProductoCreateView.as_view(), name='producto-crear'),
    path('productos/<int:id>/actualizar/', ProductoUpdateView.as_view(), name='producto-actualizar'),
    path('productos/<int:id>/eliminar/', ProductoDeleteView.as_view(), name='producto-eliminar'),

    path('categorias/<int:id>/', CategoriaDetailView.as_view(), name='categoria-detalle'),
    path('categorias/crear/', CategoriaCreateView.as_view(), name='categoria-crear'),
    path('categorias/<int:id>/actualizar/', CategoriaUpdateView.as_view(), name='categoria-actualizar'),
    path('categorias/<int:id>/eliminar/', CategoriaDeleteView.as_view(), name='categoria-eliminar'),

    path('marcas/<int:id>/', MarcaDetailView.as_view(), name='marca-detalle'),
]
