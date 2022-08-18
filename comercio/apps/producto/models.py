from tabnanny import verbose
from django.db import models

# Create your models here.

class Producto(models.Model):
  codigo = models.CharField(unique=True, verbose_name="Codigo producto", max_length=10)
  nombre = models.CharField(max_length=20,verbose_name='Nombre')
  marca = models.CharField(max_length=20,verbose_name='Marca')
  descripcion = models.TextField(max_length=200,verbose_name='Descripcion', blank=True)
  precio = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Precio')
  stock = models.PositiveSmallIntegerField(verbose_name='Stock')

  
  def __str__(self):
    return '{} - {}'.format(self.nombre, self.marca)
  
  class Meta:
    verbose_name_plural = 'Productos'
    ordering = ['nombre','marca','precio']

