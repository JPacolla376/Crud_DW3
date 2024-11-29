"""
URL configuration for suporte_chamados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página inicial
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lista_chamados/', views.lista_chamados, name='lista_chamados'),  # Página para listar chamados
    path('criar_chamado/', views.criar_chamado, name='criar_chamado'),  # Criar chamado
    path('detalhes_chamado/<int:id>/', views.detalhes_chamado, name='detalhes_chamado'),  # Detalhes do chamado
    path('editar_chamado/<int:id>/', views.editar_chamado, name='editar_chamado'),  # Editar chamado
    path('deletar_chamado/<int:id>/', views.deletar_chamado, name='deletar_chamado'),  # Deletar chamado
]




