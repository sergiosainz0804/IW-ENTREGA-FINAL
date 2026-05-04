from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='DashBoard'),
    
  
    path('Lista/', views.IncidenciaListView.as_view(), name='Listado'),
    path('Detalles/<int:pk>/', views.IncidenciaDetailView.as_view(), name='DetallesI'),
    path('Registrar/', views.Registrar, name='Registrar'),
    path('Borrar/<int:pk>/', views.Borrar, name='Borrar'),
    path('BorrarM/<int:pk>/', views.BorrarM, name='BorrarM'),
    path('BorrarP/<int:pk>/', views.BorrarP, name='BorrarP'),


   
    path('Lista_Material/', views.MaterialListView.as_view(), name='Lista_Material'),
    path('RegistrarM/', views.RegistrarM, name='RegistrarM'),
    path('DetallesM/<int:pk>/', views.MaterialDetailView.as_view(), name='DetallesM'),
    
  
    path('ListaP/', views.ProveedorListView.as_view(), name='Lista_Proveedor'),
    path('RegistrarP/', views.RegistrarP, name='RegistrarP'),
    path('DetallesP/<int:pk>/', views.ProveedorDetailView.as_view(), name='DetallesP'),

    path('Registrado/', views.Registrado, name='Registrado'),
    
    path('ModificarI/<int:pk>/', views.ModificarIncidencia, name='ModificarI'),
    path('ModificarM/<int:pk>/', views.ModificarMaterial, name='ModificarM'),
    path('ModificarP/<int:pk>/', views.ModificarProveedor, name='ModificarP')

]