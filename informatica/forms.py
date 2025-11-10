from django import forms
from .models import Docente, Material, Usuario

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['rut', 'nombre', 'email', 'activo']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'descripcion', 'stock', 'activo']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'is_active']

class PrestamoForm(forms.Form):
    docente = forms.ModelChoiceField(
        queryset=Docente.objects.filter(activo=True),
        label="Docente"
    )
    material = forms.ModelChoiceField(
        queryset=Material.objects.filter(activo=True),
        label="Material"
    )
    cantidad = forms.IntegerField(
        min_value=1,
        label="Cantidad"
    )
