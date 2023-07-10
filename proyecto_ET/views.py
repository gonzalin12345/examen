from django.shortcuts import render

def mostrar_principal(request):
    return render(request,'principal.html')