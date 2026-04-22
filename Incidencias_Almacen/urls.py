from django.urls import path
from . import views

urlpatterns = [
    path('DashBoard/', views.dashboard, name = 'DashBoard'),
    path('Lista/', views.lista, name = 'Listado' ),
    path('Detalles/', views.Detalles, name = 'Detalles'),
    
]