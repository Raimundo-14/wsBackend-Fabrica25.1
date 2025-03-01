from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listar/', views.listar_frases, name='listar_frases'),
    path('editar/<int:pk>/', views.editar_frase, name='editar_frase'),
    path('deletar/<int:pk>/', views.deletar_frase, name='deletar_frase'),
]