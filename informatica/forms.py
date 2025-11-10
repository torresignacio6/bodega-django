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
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password', 'rol']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

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
