from django.shortcuts import render

def dashboard(request):
    return render(request, 'Incidencias_Almacen/DashBoard.html')

def lista(request):
    return render(request , 'Incidencias_Almacen/lista_incidencia.html')

def Detalles(request):
    return render(request, 'Incidencias_Almacen/Detalle_Incidencia.html')

def Registrar(request):
    return render (request, 'Incidencias_Almacen/Registrar_Incidencia.html')

def Lista_Material(request):
    return render(request, 'Incidencias_Almacen/Lista_Materiales.html')

def DetallesM(request):
    return render(request, 'Incidencias_Almacen/Detalles_Material.html')