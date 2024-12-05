from django.test import TestCase
from .models import Chamado
from django.urls import reverse
from django.contrib.auth.models import User 


class ChamadoModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username="teste_user", password="senha123")
        self.chamado = Chamado.objects.create(
            titulo="Teste",
            descricao="Descrição do teste",
            solicitante=self.usuario
        )

    def test_criar_chamado(self):
        self.assertEqual(self.chamado.titulo, "Teste")
        self.assertEqual(self.chamado.descricao, "Descrição do teste")
        self.assertEqual(self.chamado.solicitante, self.usuario)
        self.assertEqual(str(self.chamado), self.chamado.titulo)

    def test_chamado_sem_titulo(self):
        with self.assertRaises(Exception):
            Chamado.objects.create(descricao="Sem título", solicitante=self.usuario)


class ViewTest(TestCase):
    def test_pagina_login_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_pagina_login_conteudo(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, "Login")

    def test_pagina_dashboard_sem_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

#python manage.py test
