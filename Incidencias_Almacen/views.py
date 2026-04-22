from django.shortcuts import render

def dashboard(request):
    return render(request, 'Incidencias_Almacen/DashBoard.html')

def lista(request):
    return render(request , 'Incidencias_Almacen/lista_incidencia.html')

def Detalles(request):
    return render(request, 'Incidencias_Almacen/Detalle_Incidencia.html')
