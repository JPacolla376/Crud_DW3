Sistema de Chamados - Projeto Escolar

Descrição
Este projeto foi desenvolvido como parte de um desafio escolar proposto pelo professor Orlando Saraiva. O objetivo principal é criar um Crud funcional e intuitivo, utilizando o framework Django para o backend e Bootstrap para a interface.

Funcionalidades
Autenticação de Usuário:

Login e Logout.
Cadastro de novos usuários.
Gestão de Chamados:

Criação de novos chamados.
Listagem de chamados existentes.
Visualização de detalhes de chamados.
Painel Administrativo:

Acompanhamento e gerenciamento de chamados.
Interface intuitiva para facilitar a navegação.
Tecnologias Utilizadas
Python: Linguagem principal para o backend.
Django: Framework web para desenvolvimento do backend.
Bootstrap: Framework de CSS para estilização e responsividade.
HTML5 e CSS3: Para estrutura e personalização da interface.
SQLite: Banco de dados utilizado para armazenamento.

Requisitos para Execução
Certifique-se de ter os seguintes pré-requisitos instalados no seu ambiente:

Python 3.10+
Pip (gerenciador de pacotes do Python)
Virtualenv (opcional, mas recomendado)

Como Executar o Projeto
Clone este repositório:

bash
Copy code
git clone https://github.com/JPacolla376/Crud_DW3.git

Crie um ambiente virtual e ative-o:

bash
Copy code
python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Configure o banco de dados:

bash
Copy code
python manage.py migrate
Inicie o servidor de desenvolvimento:

bash
Copy code
python manage.py runserver
Acesse o sistema em http://127.0.0.1:8000.
