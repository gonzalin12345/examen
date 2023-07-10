from django.urls import path
from .views import (
    agregar_productos,
    mostrar_productos, 
    agregar_carrito, carrito,
    listar_producto
)
urlpatterns = [ 
    path('', mostrar_productos, name='mostrar_productos'),
    path('nuevo_producto/',agregar_productos, name='pagina_agregar' ),
    path('carrito/', carrito, name='carrito'),
    path('agregar/<int:id_producto>/', agregar_carrito, name='agregar'),
    path('listar_producto/', listar_producto , name="listar_producto")
]