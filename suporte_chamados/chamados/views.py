from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from chamados.models import Chamado
from .forms import ChamadoForm, CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

@login_required
def lista_chamados(request):
    chamados = Chamado.objects.filter(solicitante=request.user)
    return render(request, 'lista_chamados.html', {'chamados': chamados})

@login_required
def criar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST, request.FILES)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.solicitante = request.user
            chamado.save()
            messages.success(request, 'Chamado criado com sucesso!')
            return redirect('lista_chamados')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = ChamadoForm()
    
    return render(request, 'criar_chamado.html', {'form': form})



@login_required
def detalhes_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, solicitante=request.user)
    return render(request, 'detalhes_chamado.html', {'chamado': chamado})

@login_required
def editar_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, solicitante=request.user)
    if request.method == 'POST':
        form = ChamadoForm(request.POST, request.FILES, instance=chamado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Chamado atualizado com sucesso!')
            return redirect('lista_chamados')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = ChamadoForm(instance=chamado)
    
    return render(request, 'editar_chamado.html', {'form': form})


@login_required
def deletar_chamado(request, id):
    chamado = get_object_or_404(Chamado, id=id, solicitante=request.user)
    if request.method == 'POST':
        chamado.delete()
        return redirect('lista_chamados')

    return render(request, 'deletar_chamado.html', {'chamado': chamado})

@login_required
def dashboard(request):
    chamados = Chamado.objects.filter(solicitante=request.user)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        chamados = chamados.filter(data_criacao__gte=start_date)
    
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        chamados = chamados.filter(data_criacao__lte=end_date)

    status_count = {
        'Aberto': chamados.filter(status='Aberto').count(),
        'Em andamento': chamados.filter(status='Em andamento').count(),
        'Concluído': chamados.filter(status='Concluído').count(),
        'Cancelado': chamados.filter(status='Cancelado').count(),
    }

    classification_count = {
        'Baixa': chamados.filter(classificacao='Baixa').count(),
        'Média': chamados.filter(classificacao='Média').count(),
        'Urgente': chamados.filter(classificacao='Urgente').count(),
        'Emergência': chamados.filter(classificacao='Emergência').count(),
    }

    return render(request, 'dashboard.html', {
        'status_count': status_count,
        'classification_count': classification_count,
        'start_date': start_date,
        'end_date': end_date,
    })



def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = CustomUserCreationForm()

    return render(request, 'cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Erro ao autenticar. Verifique os campos e tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@require_POST
def logout_view(request):
    logout(request)
    return redirect('index')


