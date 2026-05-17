from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.db import IntegrityError
from .models import Incidencia, Material, Proveedor , Operario
from .forms import IncidenciaForm, MaterialForm, ProveedorForm
from .serializers import IncidenciaSerializer, MaterialSerializer, ProveedorSerializer, OperarioSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout as auth_logout

#login en todas las de registro
@login_required
def Menu(request):
    refresh = RefreshToken.for_user(request.user)
    return render(request, 'Incidencias_Almacen/Menu_Registros.html', {
        'jwt_token': str(refresh.access_token)
    })

@login_required
def Registrar(request):
    refresh = RefreshToken.for_user(request.user)
    if request.method == 'POST':
        form = IncidenciaForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                Incidencia.objects.create(**form.cleaned_data)
                return redirect('Registrado')
            except IntegrityError:
                form.add_error('codigo', 'Ya existe una incidencia con este código.')
    else:
        form = IncidenciaForm()
    
    return render(request, 'Incidencias_Almacen/Registrar_Incidencia.html', {
        'form': form,
        'jwt_token': str(refresh.access_token)
    })

@login_required
def RegistrarM(request):
    refresh = RefreshToken.for_user(request.user)
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            try:
                Material.objects.create(**form.cleaned_data)
                return redirect('Registrado')
            except IntegrityError:
                form.add_error('codigo_interno', 'Ya existe un material con este código interno.')
    else:
        form = MaterialForm()

    return render(request, 'Incidencias_Almacen/Registrar_Material.html', {
        'form': form,
        'jwt_token': str(refresh.access_token)
    })


@login_required
def RegistrarP(request):
    refresh = RefreshToken.for_user(request.user)
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            try:
                Proveedor.objects.create(**form.cleaned_data)
                return redirect('Registrado')
            except IntegrityError:
                form.add_error('cif', 'Ya existe un proveedor con este CIF.')

    else:
        form = ProveedorForm()
    return render(request, 'Incidencias_Almacen/Registrar_Proveedor.html', {
        'form': form,
        'jwt_token': jwt_token
    })
#logout

def logout(request):
    auth_logout(request)
    return redirect('DashBoard')

#vista dashbiard
def dashboard(request):
    ultimas_incidencias = Incidencia.objects.order_by('-fecha_alta')[:5]
    return render(request, 'Incidencias_Almacen/DashBoard.html', {'ultimas_incidencias': ultimas_incidencias})

#incidencias
class IncidenciaListView(ListView):
    model = Incidencia
    template_name = 'Incidencias_Almacen/lista_incidencia.html'
    context_object_name = 'incidencias'

    def get_queryset(self):
        consulta = Incidencia.objects.all().order_by('titulo')
        q = self.request.GET.get('q')
        prioridad = self.request.GET.get('prioridad')
        estado = self.request.GET.get('estado')

        if q:
            consulta = consulta.filter(
                Q(codigo__icontains=q) | 
                Q(titulo__icontains=q) | 
                Q(descripcion_detallada__icontains=q) |
                Q(zona_almacen__icontains=q)
            )
        
        if prioridad:
            consulta = consulta.filter(nivel_prioridad=prioridad)
        
        if estado:
            consulta = consulta.filter(estado=estado)

        return consulta

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

    def get_queryset(self):
        consulta = Material.objects.all().order_by('nombre')
        q = self.request.GET.get('q')
        familia = self.request.GET.get('familia')

        if q:
            consulta = consulta.filter(
                Q(codigo_interno__icontains=q) | 
                Q(nombre__icontains=q) | 
                Q(descripcion__icontains=q) |
                Q(ubicacion_habitual__icontains=q)
            )
        
        if familia:
            consulta = consulta.filter(familia__icontains=familia)

        return consulta

class MaterialDetailView(DetailView):
    model = Material
    template_name = 'Incidencias_Almacen/Detalles_Material.html'
    context_object_name = 'material'



#Proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'Incidencias_Almacen/Lista_Proveedores.html'
    context_object_name = 'proveedores'

    def get_queryset(self):
        consulta = Proveedor.objects.all().order_by('nombre_comercial')
        q = self.request.GET.get('q')

        if q:
            consulta = consulta.filter(
                Q(cif__icontains=q) | 
                Q(nombre_comercial__icontains=q) | 
                Q(email__icontains=q) |
                Q(direccion__icontains=q)
            )

        return consulta

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'Incidencias_Almacen/Detalles_Proveedor.html'
    context_object_name = 'proveedor'


def Registrado(request):
    
    return render(request, 'Incidencias_Almacen/Registrado.html')

def ModificarIncidencia(request, pk):

    inci = get_object_or_404(Incidencia, pk = pk)

    if request.method == 'POST':

        form = IncidenciaForm(request.POST, request.FILES)
        if form.is_valid():
           
            inci.codigo = form.cleaned_data['codigo']
            inci.titulo = form.cleaned_data['titulo']
            inci.descripcion_detallada = form.cleaned_data['descripcion_detallada']
            inci.estado = form.cleaned_data['estado']
            inci.nivel_prioridad = form.cleaned_data['nivel_prioridad']
            inci.zona_almacen = form.cleaned_data['zona_almacen']
            inci.operario_asignado = form.cleaned_data['operario_asignado']
            inci.material_afectado = form.cleaned_data['material_afectado']
            inci.documento_adjunto = form.cleaned_data['documento_adjunto']
        
            try:
                inci.save()
                return redirect('Listado')
            except IntegrityError:
                form.add_error('codigo', 'Ya existe una incidencia con este código.')
    
    else:
        form = IncidenciaForm(initial={ 
            'codigo': inci.codigo,
            'titulo': inci.titulo,
            'descripcion_detallada': inci.descripcion_detallada,
            'estado': inci.estado,
            'nivel_prioridad': inci.nivel_prioridad,
            'zona_almacen': inci.zona_almacen,
            'operario_asignado': inci.operario_asignado,
            'material_afectado': inci.material_afectado,
            'documento_adjunto': inci.documento_adjunto,
        })
    return render(request, 'Incidencias_Almacen/Modificar_Incidencia.html', {'form': form})

def ModificarMaterial(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material.codigo_interno = form.cleaned_data['codigo_interno']
            material.nombre = form.cleaned_data['nombre']
            material.descripcion = form.cleaned_data['descripcion']
            material.familia = form.cleaned_data['familia']
            material.ubicacion_habitual = form.cleaned_data['ubicacion_habitual']
            material.proveedor_principal = form.cleaned_data['proveedor_principal']
            
            try:
                material.save()
                return redirect('Lista_Material')
            except IntegrityError:
                form.add_error('codigo_interno', 'Ya existe un material con este código interno.')
    else:
        form = MaterialForm(initial={
            'codigo_interno': material.codigo_interno,
            'nombre': material.nombre,
            'descripcion': material.descripcion,
            'familia': material.familia,
            'ubicacion_habitual': material.ubicacion_habitual,
            'proveedor_principal': material.proveedor_principal,
        })
    return render(request, 'Incidencias_Almacen/Modificar_Material.html', {'form': form})

def ModificarProveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor.cif = form.cleaned_data['cif']
            proveedor.nombre_comercial = form.cleaned_data['nombre_comercial']
            proveedor.email = form.cleaned_data['email']
            proveedor.telefono = form.cleaned_data['telefono']
            proveedor.direccion = form.cleaned_data['direccion']
            
            try:
                proveedor.save()
                return redirect('Lista_Proveedor')
            except IntegrityError:
                form.add_error('cif', 'Ya existe un proveedor con este CIF.')
    else:
        form = ProveedorForm(initial={
            'cif': proveedor.cif,
            'nombre_comercial': proveedor.nombre_comercial,
            'email': proveedor.email,
            'telefono': proveedor.telefono,
            'direccion': proveedor.direccion,
        })
    return render(request, 'Incidencias_Almacen/Modificar_Proveedor.html', {'form': form})

def BorrarM(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('Lista_Material')
    return render(request, 'Incidencias_Almacen/confirmar_borrado_material.html', {'material': material})

def BorrarP(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('Lista_Proveedor')
    return render(request, 'Incidencias_Almacen/confirmar_borrado_proveedor.html', {'proveedor': proveedor})





#serializacion

class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class OperarioViewSet(viewsets.ModelViewSet):
    queryset = Operario.objects.all()
    serializer_class = OperarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

