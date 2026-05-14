from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'Incidencias', views.IncidenciaViewSet, basename = 'Incidencias')
router.register(r'Materiales', views.MaterialViewSet, basename = 'Materiales')
router.register(r'Proveedores', views.ProveedorViewSet, basename = 'Proveedores')
router.register(r'Operarios', views.OperarioViewSet, basename = 'Operarios')
urlpatterns = [
    path('Incidencias_API/', include(router.urls)),
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
    path('ModificarP/<int:pk>/', views.ModificarProveedor, name='ModificarP'),

    #Login
    path('Login/', auth_views.LoginView.as_view(template_name='Incidencias_Almacen/Login.html'), name='Login'),
    path('Menu/', views.Menu, name = 'Menu'),

    #Logout
    path('DashboardL/', views.logout, name = 'logout'),


    #JWT

    path('api/token/', TokenObtainPairView.as_view(), name = 'obtener_token'),
    path('api/token/refresh', TokenRefreshView.as_view() , name = 'refresh_token')

]