from django.urls import path
from . import views

urlpatterns = [
    path('DashBoard/', views.dashboard, name = 'DashBoard'),
]