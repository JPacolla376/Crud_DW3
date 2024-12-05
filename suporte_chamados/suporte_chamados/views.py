from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from chamados.models import Chamado




# Página inicial
def index(request):
    return render(request, 'index.html')

# Listar chamados
@login_required
def lista_chamados(request):
    chamados = Chamado.objects.filter(solicitante=request.user)
    return render(request, 'lista_chamados.html', {'chamados': chamados})

# Criar chamado
@login_required
def criar_chamado(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        classificacao = request.POST.get('classificacao')
        anexo = request.FILES.get('anexo')
        data_vencimento = request.POST.get('data_vencimento')

        chamado = Chamado.objects.create(
            titulo=titulo,
            descricao=descricao,
            classificacao=classificacao,
            anexo=anexo,
            data_vencimento=data_vencimento,
            solicitante=request.user
        )
        return redirect('lista_chamados')

    return render(request, 'criar_chamado.html')

# Detalhes do chamado
@login_required
def detalhes_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, solicitante=request.user)
    return render(request, 'detalhes_chamado.html', {'chamado': chamado})

# Editar chamado
@login_required
def editar_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, solicitante=request.user)

    if request.method == 'POST':
        chamado.titulo = request.POST.get('titulo')
        chamado.descricao = request.POST.get('descricao')
        chamado.classificacao = request.POST.get('classificacao')
        chamado.data_vencimento = request.POST.get('data_vencimento')
        chamado.save()
        return redirect('lista_chamados')

    return render(request, 'editar_chamado.html', {'chamado': chamado})

# Deletar chamado
@login_required
def deletar_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, solicitante=request.user)
    if request.method == 'POST':
        chamado.delete()
        return redirect('lista_chamados')

    return render(request, 'deletar_chamado.html', {'chamado': chamado})

# Dashboard
@login_required
def dashboard(request):
    chamados = Chamado.objects.all()

    # Estatísticas
    status_count = {
        'Aberto': chamados.filter(status='Aberto').count(),
        'Em andamento': chamados.filter(status='Em andamento').count(),
        'Concluído': chamados.filter(status='Concluído').count(),
        'Cancelado': chamados.filter(status='Cancelado').count(),
    }

    return render(request, 'dashboard.html', {'status_count': status_count})

# Cadastro
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})
