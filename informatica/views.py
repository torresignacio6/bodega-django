from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Docente, Material, Usuario, Prestamo, DetallePrestamo
from .forms import DocenteForm, MaterialForm, UsuarioForm, PrestamoForm
from .decorators import rol_requerido

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')

@rol_requerido('ADMIN')
def docente_list(request):
    docentes = Docente.objects.all()
    return render(request, 'docente_list.html', {'docentes': docentes})


@rol_requerido('ADMIN')
def docente_create(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docente_list')
    else:
        form = DocenteForm()
    return render(request, 'docente_form.html', {'form': form, 'titulo': 'Crear docente'})


@rol_requerido('ADMIN')
def docente_update(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('docente_list')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'docente_form.html', {'form': form, 'titulo': 'Editar docente'})


@rol_requerido('ADMIN')
def docente_delete(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('docente_list')
    return render(request, 'docente_confirm_delete.html', {'docente': docente})

@rol_requerido('ADMIN')
def material_list(request):
    materiales = Material.objects.all()
    return render(request, 'material_list.html', {'materiales': materiales})


@rol_requerido('ADMIN')
def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'material_form.html', {'form': form, 'titulo': 'Crear material'})


@rol_requerido('ADMIN')
def material_update(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material_form.html', {'form': form, 'titulo': 'Editar material'})


@rol_requerido('ADMIN')
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('material_list')
    return render(request, 'material_confirm_delete.html', {'material': material})

@rol_requerido('ADMIN')
def admin_user_list(request):
    usuarios = Usuario.objects.filter(rol='ADMIN')
    return render(request, 'admin_user_list.html', {'usuarios': usuarios})


@rol_requerido('ADMIN')
def admin_user_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = 'ADMIN'
            user.save()
            return redirect('admin_user_list')
    else:
        form = UsuarioForm()
    return render(request, 'admin_user_form.html', {
        'form': form,
        'titulo': 'Crear administrador'
    })


@rol_requerido('ADMIN')
def admin_user_update(request, pk):
    user = get_object_or_404(Usuario, pk=pk, rol='ADMIN')
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = 'ADMIN'
            user.save()
            return redirect('admin_user_list')
    else:
        form = UsuarioForm(instance=user)
    return render(request, 'admin_user_form.html', {
        'form': form,
        'titulo': 'Editar administrador'
    })


@rol_requerido('ADMIN')
def admin_user_delete(request, pk):
    user = get_object_or_404(Usuario, pk=pk, rol='ADMIN')
    if request.method == 'POST':
        user.delete()
        return redirect('admin_user_list')
    return render(request, 'admin_user_confirm_delete.html', {'usuario': user})

@rol_requerido('ADMIN')
def panol_user_list(request):
    usuarios = Usuario.objects.filter(rol='PANOL')
    return render(request, 'panol_user_list.html', {'usuarios': usuarios})


@rol_requerido('ADMIN')
def panol_user_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = 'PANOL'
            user.save()
            return redirect('panol_user_list')
    else:
        form = UsuarioForm()
    return render(request, 'panol_user_form.html', {
        'form': form,
        'titulo': 'Crear usuario de pañol'
    })


@rol_requerido('ADMIN')
def panol_user_update(request, pk):
    user = get_object_or_404(Usuario, pk=pk, rol='PANOL')
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = 'PANOL'
            user.save()
            return redirect('panol_user_list')
    else:
        form = UsuarioForm(instance=user)
    return render(request, 'panol_user_form.html', {
        'form': form,
        'titulo': 'Editar usuario de pañol'
    })


@rol_requerido('ADMIN')
def panol_user_delete(request, pk):
    user = get_object_or_404(Usuario, pk=pk, rol='PANOL')
    if request.method == 'POST':
        user.delete()
        return redirect('panol_user_list')
    return render(request, 'panol_user_confirm_delete.html', {'usuario': user})

@rol_requerido('PANOL')
def registrar_prestamo(request):
    materiales = Material.objects.filter(activo=True)
    mensaje = None
    error = None

    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            docente = form.cleaned_data['docente']
            material = form.cleaned_data['material']
            cantidad = form.cleaned_data['cantidad']

            if material.stock < cantidad:
                error = f"No hay stock suficiente. Stock actual: {material.stock}."
            else:
                prestamo = Prestamo.objects.create(docente=docente, panol=request.user)
                DetallePrestamo.objects.create(prestamo=prestamo, material=material, cantidad=cantidad)
                material.stock -= cantidad
                material.save()
                mensaje = "Préstamo registrado correctamente."
                form = PrestamoForm()
    else:
        form = PrestamoForm()

    return render(request, 'registrar_prestamo.html', {
        'form': form,
        'materiales': materiales,
        'mensaje': mensaje,
        'error': error,
    })


@rol_requerido('PANOL')
def prestamo_list(request):
    prestamos = (
        Prestamo.objects
        .select_related('docente', 'panol')
        .prefetch_related('detalles__material')
        .order_by('-fecha')
    )
    return render(request, 'prestamo_list.html', {'prestamos': prestamos})


@login_required
def admin_prestamos_list(request):
    prestamos = (
        Prestamo.objects
        .select_related('docente', 'panol')
        .prefetch_related('detalles__material')
        .order_by('-fecha')
    )
    return render(request, 'admin_prestamos_list.html', {'prestamos': prestamos})


@login_required
def admin_prestamo_delete(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    prestamo.delete()
    return redirect('admin_prestamos_list')
