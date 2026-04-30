from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Incidencia, Material, Proveedor
from .forms import IncidenciaForm, MaterialForm, ProveedorForm

#vista dashbiard
def dashboard(request):
    ultimas_incidencias = Incidencia.objects.order_by('-fecha_alta')[:5]
    return render(request, 'Incidencias_Almacen/DashBoard.html', {'ultimas_incidencias': ultimas_incidencias})

#incidencias
class IncidenciaListView(ListView):
    model = Incidencia
    template_name = 'Incidencias_Almacen/lista_incidencia.html'
    context_object_name = 'incidencias'
    queryset = Incidencia.objects.order_by('titulo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_incidencias'] = Incidencia.objects.count()
        context['incidencias_baja'] = Incidencia.objects.filter(nivel_prioridad='BAJA').count()
        context['incidencias_media'] = Incidencia.objects.filter(nivel_prioridad='MEDIA').count()
        context['incidencias_alta'] = Incidencia.objects.filter(nivel_prioridad='ALTA').count()
        context['incidencias_urgente'] = Incidencia.objects.filter(nivel_prioridad='URGENTE').count()
        return context

class IncidenciaDetailView(DetailView):
    model = Incidencia
    template_name = 'Incidencias_Almacen/Detalle_Incidencia.html'
    context_object_name = 'incidencia'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la Incidencia'
        return context

def Registrar(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            Incidencia.objects.create(**form.cleaned_data)
            return redirect('Registrado')
    else:
        form = IncidenciaForm()
    return render(request, 'Incidencias_Almacen/Registrar_Incidencia.html', {'form': form})

def Borrar(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)
    if request.method == 'POST':
        incidencia.delete()
        return redirect('DashBoard')
    return render(request, 'Incidencias_Almacen/confirmar_borrado.html', {'incidencia': incidencia})

#Materiales
class MaterialListView(ListView):
    model = Material
    template_name = 'Incidencias_Almacen/Lista_Materiales.html'
    context_object_name = 'materiales'
    queryset = Material.objects.order_by('nombre')

class MaterialDetailView(DetailView):
    model = Material
    template_name = 'Incidencias_Almacen/Detalles_Material.html'
    context_object_name = 'material'

def RegistrarM(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            Material.objects.create(**form.cleaned_data)
            return redirect('Registrado')

    else:
        form = MaterialForm()
    return render(request, 'Incidencias_Almacen/Registrar_Material.html', {'form': form})

#Proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'Incidencias_Almacen/Lista_Proveedores.html'
    context_object_name = 'proveedores'
    queryset = Proveedor.objects.order_by('nombre_comercial')

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'Incidencias_Almacen/Detalles_Proveedor.html'
    context_object_name = 'proveedor'

def RegistrarP(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data['nombre_comercial']
            Proveedor.objects.create(**form.cleaned_data)
            return redirect('Registrado')

    else:
        form = ProveedorForm()
    return render(request, 'Incidencias_Almacen/Registrar_Proveedor.html', {'form': form})

def Registrado(request):
    
    return render(request, 'Incidencias_Almacen/Registrado.html')