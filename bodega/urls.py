from django.contrib import admin
from django.urls import path
from informatica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('docentes/', views.docente_list, name='docente_list'),
    path('docentes/nuevo/', views.docente_create, name='docente_create'),
    path('docentes/<int:pk>/editar/', views.docente_update, name='docente_update'),
    path('docentes/<int:pk>/eliminar/', views.docente_delete, name='docente_delete'),
    path('materiales/', views.material_list, name='material_list'),
    path('materiales/nuevo/', views.material_create, name='material_create'),
    path('materiales/<int:pk>/editar/', views.material_update, name='material_update'),
    path('materiales/<int:pk>/eliminar/', views.material_delete, name='material_delete'),
    path('admins/', views.admin_user_list, name='admin_user_list'),
    path('admins/nuevo/', views.admin_user_create, name='admin_user_create'),
    path('admins/<int:pk>/editar/', views.admin_user_update, name='admin_user_update'),
    path('admins/<int:pk>/eliminar/', views.admin_user_delete, name='admin_user_delete'),
    path('panoles/', views.panol_user_list, name='panol_user_list'),
    path('panoles/nuevo/', views.panol_user_create, name='panol_user_create'),
    path('panoles/<int:pk>/editar/', views.panol_user_update, name='panol_user_update'),
    path('panoles/<int:pk>/eliminar/', views.panol_user_delete, name='panol_user_delete'),
    path('prestamos/', views.prestamo_list, name='prestamo_list'),
    path('prestamos/nuevo/', views.registrar_prestamo, name='registrar_prestamo'),
]
