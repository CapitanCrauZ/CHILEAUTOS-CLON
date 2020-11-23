from django import forms
from .models import Auto, Categoria

class AutoForm(forms.ModelForm):
    class Meta:

        model = Auto
        fields = ('nombre', 'modelo', 'marca', 'detalle', 'anio', 'precio', 'categoria','imagenAuto',)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ('name',)