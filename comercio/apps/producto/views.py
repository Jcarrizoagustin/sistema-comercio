from django.shortcuts import render
from django.views import generic
from .models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductoForm
from django.urls import reverse_lazy
# Create your views here.

class ListadoProductos(LoginRequiredMixin, generic.ListView):
  model = Producto
  template_name: str = 'producto/listado_productos.html'
  context_object_name = 'obj'
  login_url = 'inicio:login'
  
class AgregarProducto(LoginRequiredMixin, generic.CreateView):
  model = Producto
  template_name = 'producto/agregar_producto.html'
  form_class = ProductoForm
  success_url =reverse_lazy('producto:listadoproductos')
  login_url = 'inicio:login'
  
class EditarProducto(LoginRequiredMixin, generic.UpdateView):
  model = Producto
  template_name= 'producto/editar_producto.html'
  form_class =  ProductoForm
  success_url =reverse_lazy('producto:listadoproductos')
  login_url = 'inicio:login'
  context_object_name = 'obj'