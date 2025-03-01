from django.contrib import admin
from django.urls import path, include
from appfrase import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appfrase.urls')),
    path('listar/', include('appfrase.urls')),
    path('editar/<int:pk>/', views.editar_frase, name='editar_frase'),
    path('deletar/<int:pk>/', views.deletar_frase, name='deletar_frase'),
]
