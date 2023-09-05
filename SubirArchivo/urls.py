from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('subir/', views.uploadFile, name='uploadFile'),
    path('archivos/', views.lista_archivo, name='lista_archivo'),
]
