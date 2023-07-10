from django.shortcuts import render, redirect
from .forms import Registro, Entrar
from sweetify import info, success, warning, error
from django.contrib.auth import authenticate, login ,logout

# Create your views here.

def mostrar_registro(request):
    if request.method == 'GET':
        contexto = {
            'Registrar': Registro()
        }
        return render(request, 'registro.html', contexto)
    if request.method == 'POST':
        form_registro = Registro(data=request.POST)
        es_valido = form_registro.is_valid() # Retorna un bool
        if es_valido: # Si bool es True
            nuevo_usuario = form_registro.save()
            success(request,'Bienvenido')
            return redirect('pagina_principal')
        contexto = {
            'Registrar': form_registro
        }
        warning(request,'revise los errores e intente denuevo')
        return render(request,'registro.html',contexto)
def mostrar_login(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'Entrar':Entrar(),
        }
        return render(request,'iniciar_sesion.html',contexto)
    if request.method == 'POST':
        datos_usuario = Entrar(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            usuario = authenticate(
                username = datos_usuario.cleaned_data['usuario'],
                password = datos_usuario.cleaned_data['contrasenia_usuario']
            )
            if usuario is not None:
                login(request, usuario)
                success(request, f'Bienvenido {usuario.username}')
                return redirect('pagina_principal')
        warning(request, 'Usuario o contraseña invalidos')
        contexto = {
            'Entrar': datos_usuario
        }
        return render(request,'iniciar_sesion.html', contexto)
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(request, 'Sesion cerrada')
    return redirect('pagina_principal')




