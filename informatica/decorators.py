from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def rol_requerido(rol):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if getattr(request.user, 'rol', None) == rol:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        return _wrapped_view
    return decorator
