Proyecto base EVA3 - Bodega Informática

Pasos rápidos:

1) Crear entorno virtual:
   python -m venv venv
   venv\Scripts\activate   (Windows)

2) Instalar dependencias:
   pip install -r requirements.txt

3) Aplicar migraciones:
   python manage.py makemigrations
   python manage.py migrate

4) Crear superusuario:
   python manage.py createsuperuser

5) Ejecutar servidor:
   python manage.py runserver

Luego entra a:
   http://127.0.0.1:8000/

y a:
   http://127.0.0.1:8000/admin/

IMPORTANTE:
- Por defecto usa SQLite para que funcione al tiro.
- Para la evaluación, cambia DATABASES en bodega/settings.py
  a PostgreSQL apuntando a tu servidor (local o EC2).
