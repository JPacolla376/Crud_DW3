from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
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