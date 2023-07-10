from django.urls import path
from .views import mostrar_registro, mostrar_login, cerrar_sesion

urlpatterns = [path('registrar/',mostrar_registro, name='mostrar_registro'),
               path('entrar/',mostrar_login, name='mostrar_login'),
               path('cerrar/',cerrar_sesion, name='cerrar_sesion')
            ]    