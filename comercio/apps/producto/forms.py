from pyexpat import model
from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
  class Meta:
    model = Producto
    fields = ('__all__')
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control',
      })