from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ListadoProductos(LoginRequiredMixin, generic.TemplateView):
  template_name = "producto/listado_productos.html"
  login_url = 'inicio:login'