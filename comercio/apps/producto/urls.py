from django.urls import path
from .views import ListadoProductos, AgregarProducto, EditarProducto
urlpatterns = [
  path("listadoproductos/",ListadoProductos.as_view(),name='listadoproductos'),
  path("nuevoproducto/", AgregarProducto.as_view(), name='agregarproducto'),
  path("editarproducto/<int:pk>", EditarProducto.as_view(), name='editarproducto'),
]