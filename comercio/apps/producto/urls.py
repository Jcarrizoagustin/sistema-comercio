from django.urls import path
from .views import ListadoProductos
urlpatterns = [
  path("listadoproductos/",ListadoProductos.as_view(),name='listadoproductos'),
]