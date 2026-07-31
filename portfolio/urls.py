from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lista_projetos/', views.lista_projetos, name='lista_projetos'),
    path('projeto/<int:id_projeto>/',views.detalhes_projeto, name="detalhes_projeto")
]