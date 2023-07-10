from django.shortcuts import render, redirect
from .forms import FormularioProducto
from django.contrib.auth.decorators import login_required
from sweetify import success, warning
from .models import ModeloProducto, Boleta , Detalle_boleta
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def es_superusuario(user):
    return user.is_superuser

@user_passes_test(es_superusuario)

def agregar_productos(request):
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            success(request, "Guardado correctamente")
            return redirect("mostrar_productos")
    else:
        formulario = FormularioProducto()

    contexto = {
        'agregar': formulario
    }

    return render(request, 'productos/agregar.html', contexto)



def mostrar_productos(request):
    todos_los_productos = ModeloProducto.objects.all()
    contexto = {
        'listar': todos_los_productos
    }
    return render(request, 'productos/listar.html', contexto)

@login_required
def carrito(request):
    producto = ModeloProducto.objects.all()
    estado = Boleta.estado = True
    contexto={
        'carrito': producto
    }
    return render(request, 'productos/carrito.html', contexto)

@login_required
def agregar_carrito (request, id_producto):
    boleta_actual = None
    try :
        boleta_actual = Boleta.objects.get(usuario__id = request.user.id, estado = False)
    except Boleta.DoesNotExist:
        nueva_boleta = Boleta ()
        nueva_boleta.total = 0 
        nueva_boleta.estado = False 
        nueva_boleta.usuario = request.user
        boleta_actual = nueva_boleta.save()
    producto_elegido = ModeloProducto.objects.get(id = id_producto)
    try :
        actual = Detalle_boleta.objects.get(boleta__id = boleta_actual.id , producto__id = id_producto)
        actual.cantidad = actual.cantidad + 1
        actual.precio = producto_elegido.precio * actual.cantidad 
        actual.save()
    except Detalle_boleta.DoesNotExist:
        nuevo_detalle = Detalle_boleta()
        nuevo_detalle.cantidad = 1
        nuevo_detalle.precio = producto_elegido.precio
        nuevo_detalle.boleta = boleta_actual
        nuevo_detalle.producto = producto_elegido
        nuevo_detalle.save()
    success(request,f"Producto {producto_elegido.nombre} Agregado")
    return redirect("carrito")

@user_passes_test(es_superusuario)
def listar_producto(request):
    productos = ModeloProducto.objects.all()

    contexto ={
        'productos' : productos
    }
    return render(request, 'productos/historial.html', contexto)