from django.forms import ModelForm
from django import forms

from .models import ModeloProducto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = ModeloProducto
        fields = '__all__'