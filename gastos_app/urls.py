from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('modo-invitado/', views.modo_invitado, name='modo_invitado'),
    path('inicio/', views.inicio, name='inicio'),
    path('agregar-gasto/', views.agregar_gasto, name='agregar_gasto'),
    path('agregar-ingreso/', views.agregar_ingreso, name='agregar_ingreso'),
    path('eliminar-movimiento/<int:movimiento_id>/', views.eliminar_movimiento, name='eliminar_movimiento'),
    path('volver-login/', views.volver_login, name='volver_login'),
]