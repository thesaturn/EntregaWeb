from django import forms

from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
        'marca',
        'modelo',
        'año',
        'color',
        'número_Puertas',
        'descripción',
        'precio',
        ]
