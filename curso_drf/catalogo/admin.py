from django.contrib import admin
from .models import Producto  # Elimina "Categoria" si no lo tienes definido

admin.site.register(Producto)
