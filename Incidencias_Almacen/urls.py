from django.urls import path
from . import views

urlpatterns = [
    path('DashBoard/', views.dashboard, name='DashBoard'),
    
  
    path('Lista/', views.IncidenciaListView.as_view(), name='Listado'),
    path('Detalles/<int:pk>/', views.IncidenciaDetailView.as_view(), name='DetallesI'),
    path('Registrar/', views.Registrar, name='Registrar'),
    path('Borrar/<int:pk>/', views.Borrar, name='Borrar'),
    
   
    path('Lista_Material/', views.MaterialListView.as_view(), name='Lista_Material'),
    path('RegistrarM/', views.RegistrarM, name='RegistrarM'),
    path('DetallesM/<int:pk>/', views.MaterialDetailView.as_view(), name='DetallesM'),
    
  
    path('ListaP/', views.ProveedorListView.as_view(), name='Lista_Proveedor'),
    path('RegistrarP/', views.RegistrarP, name='RegistrarP'),
    path('DetallesP/<int:pk>/', views.ProveedorDetailView.as_view(), name='DetallesP'),
]