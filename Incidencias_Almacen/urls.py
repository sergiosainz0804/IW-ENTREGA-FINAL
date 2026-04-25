from django.urls import path
from . import views

urlpatterns = [
    path('DashBoard/', views.dashboard, name = 'DashBoard'),
    path('Lista/', views.lista, name = 'Listado' ),
    path('Detalles/', views.Detalles, name = 'Detalles'),
    path('Registrar/', views.Registrar, name = 'Registrar'),
    path('Lista_Material/', views.Lista_Material, name= 'Lista_Material'),
    path('DetallesM/', views.DetallesM , name = 'DetalleM'),

]