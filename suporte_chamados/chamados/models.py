from django.db import models
from django.contrib.auth.models import User

class Chamado(models.Model):
    STATUS_CHOICES = [
        ('Aberto', 'Aberto'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    CLASSIFICACAO_CHOICES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Urgente', 'Urgente'),
        ('Emergência', 'Emergência'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    anexo = models.FileField(upload_to='anexos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_vencimento = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aberto')
    classificacao = models.CharField(max_length=20, choices=CLASSIFICACAO_CHOICES, default='Baixa')
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chamados')
    analista = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='analises')

    def __str__(self):
        return self.titulo
