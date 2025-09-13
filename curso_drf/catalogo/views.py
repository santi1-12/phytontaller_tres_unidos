from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, Categoria, Marca
from .serializers import ProductoSerializer, CategoriaSerializer, MarcaSerializer

# ------------------- PRODUCTOS -------------------

class ProductoListView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)


class ProductoDetailView(APIView):
    def get(self, request, id):
        try:
            producto = Producto.objects.get(pk=id)
            serializer = ProductoSerializer(producto)
            return Response(serializer.data)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)


class ProductoCreateView(APIView):
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoUpdateView(APIView):
    def put(self, request, id):
        try:
            producto = Producto.objects.get(pk=id)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDeleteView(APIView):
    def delete(self, request, id):
        try:
            producto = Producto.objects.get(pk=id)
            producto.delete()
            return Response({"mensaje": "Producto eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)


# ------------------- CATEGORIAS -------------------

class CategoriaDetailView(APIView):
    def get(self, request, id):
        try:
            categoria = Categoria.objects.get(pk=id)
            serializer = CategoriaSerializer(categoria)
            return Response(serializer.data)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoría no encontrada"}, status=status.HTTP_404_NOT_FOUND)


class CategoriaCreateView(APIView):
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaUpdateView(APIView):
    def put(self, request, id):
        try:
            categoria = Categoria.objects.get(pk=id)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoría no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDeleteView(APIView):
    def delete(self, request, id):
        try:
            categoria = Categoria.objects.get(pk=id)
            categoria.delete()
            return Response({"mensaje": "Categoría eliminada con éxito"}, status=status.HTTP_204_NO_CONTENT)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoría no encontrada"}, status=status.HTTP_404_NOT_FOUND)


# ------------------- MARCAS -------------------

class MarcaDetailView(APIView):
    def get(self, request, id):
        try:
            marca = Marca.objects.get(pk=id)
            serializer = MarcaSerializer(marca)
            return Response(serializer.data)
        except Marca.DoesNotExist:
            return Response({"error": "Marca no encontrada"}, status=status.HTTP_404_NOT_FOUND)


class MarcaCreateView(APIView):
    def post(self, request):
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarcaUpdateView(APIView):
    def put(self, request, id):
        try:
            marca = Marca.objects.get(pk=id)
        except Marca.DoesNotExist:
            return Response({"error": "Marca no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarcaDeleteView(APIView):
    def delete(self, request, id):
        try:
            marca = Marca.objects.get(pk=id)
            marca.delete()
            return Response({"mensaje": "Marca eliminada con éxito"}, status=status.HTTP_204_NO_CONTENT)
        except Marca.DoesNotExist:
            return Response({"error": "Marca no encontrada"}, status=status.HTTP_404_NOT_FOUND)
