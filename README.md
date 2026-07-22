<div align="center">
📝 TaskFlow
Sistema de Gerenciamento de Tarefas
![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=3B82F6&center=true&vCenter=true&width=500&lines=Organize+suas+tarefas+com+facilidade;Dashboard+%2B+CRUD+%2B+Relat%C3%B3rios;Modo+Claro+e+Escuro+inclusos!)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.7-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Produção-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square)
![Licença](https://img.shields.io/badge/licença-pessoal%2Feducacional-lightgrey?style=flat-square)
![Última atualização](https://img.shields.io/badge/última%20atualização-julho%202026-blue?style=flat-square)
🔗 Acesse o site no ar »
</div>
> ⚠️ **Nota sobre o plano gratuito:** o projeto está hospedado no plano free do Render. Se o site ficar 15 minutos sem receber visitas, ele entra em modo "soneca" 😴 — a primeira requisição depois disso pode demorar de 30 a 60 segundos para responder. É normal, não é um bug!
---
📖 Sobre o projeto
O TaskFlow é um sistema web completo para organização pessoal de tarefas, desenvolvido em Django. Ele foi criado com o objetivo de unir simplicidade e produtividade: cada usuário tem sua própria conta, seu próprio painel de controle e consegue acompanhar tudo o que precisa fazer de forma visual e organizada.
O projeto está em constante evolução — a ideia é que ele siga crescendo com novas funcionalidades (como projetos, calendário integrado e mais).
---
✨ Funcionalidades
🔐 Autenticação de usuários
Cada pessoa cria sua própria conta e só tem acesso às suas próprias tarefas. Sistema de cadastro, login e logout usando a autenticação nativa e segura do Django.
📊 Dashboard interativo
Assim que você entra no sistema, é recebido por um painel com:
Contagem de tarefas pendentes, em andamento, concluídas e atrasadas
Círculo de progresso mostrando o percentual de conclusão geral
Lista das próximas tarefas por prazo
✅ Gerenciamento de tarefas (CRUD completo)
Criar novas tarefas com título, descrição, prazo, prioridade e etiqueta
Listar todas as tarefas com filtros por status, prioridade e busca por palavra-chave
Editar qualquer informação de uma tarefa já existente
Excluir tarefas que não são mais necessárias (com confirmação de segurança)
📈 Relatórios
Uma visão consolidada de tudo:
Total de tarefas agrupadas por status e por prioridade
Lista de tarefas atrasadas, para você nunca perder o prazo
Resumo por etiqueta, útil para quem organiza tarefas por categoria/projeto
🌗 Modo claro e escuro
Alterne entre os temas com um clique — a preferência fica salva no seu navegador, então da próxima vez que você visitar o site, ele já abre no tema que você escolheu.
---
🛠️ Tecnologias utilizadas
Camada	Tecnologia
Backend	Python 3.14 + Django 6.0.7 + Django REST Framework
Banco de dados	SQLite (desenvolvimento) / PostgreSQL (produção)
Frontend	HTML5, CSS3 e JavaScript puro
Ícones	Bootstrap Icons
Servidor de produção	Gunicorn + WhiteNoise
Hospedagem	Render
Controle de versão	Git + GitHub
---
🚀 Como rodar o projeto localmente
Quer rodar o TaskFlow na sua própria máquina? Siga o passo a passo abaixo com calma — está bem detalhado, então mesmo quem nunca configurou um projeto Django antes consegue seguir.
✅ Pré-requisitos
Antes de começar, confirme que você tem instalado:
🐍 Python 3.13 ou superior
🔧 Git
1️⃣ Clonar o repositório
Abra o terminal (cmd, PowerShell ou terminal do seu editor de código) e rode:
```bash
git clone https://github.com/PaNiiCz/sistema_tarefas.git
cd sistema_tarefas
```
Isso baixa uma cópia completa do projeto para o seu computador e entra na pasta dele.
2️⃣ Criar e ativar o ambiente virtual (venv)
O ambiente virtual mantém as bibliotecas deste projeto separadas das bibliotecas do resto do seu computador — isso evita conflitos entre projetos diferentes.
Criar a venv:
```bash
python -m venv .venv
```
Ativar a venv:
Sistema	Comando
Windows (PowerShell)	`.venv\Scripts\Activate.ps1`
Windows (cmd)	`.venv\Scripts\activate.bat`
Linux / macOS	`source .venv/bin/activate`
💡 Você saberá que funcionou quando aparecer `(.venv)` no começo da linha do terminal.
3️⃣ Instalar as dependências
Com a venv ativada, rode:
```bash
pip install -r requirements.txt
```
Esse comando lê o arquivo `requirements.txt` e instala automaticamente todas as bibliotecas que o projeto precisa (Django, gunicorn, whitenoise, etc.) — não é necessário instalar nada manualmente.
4️⃣ Criar o arquivo de variáveis de ambiente
Crie um arquivo chamado `.env` (exatamente assim, com ponto na frente e sem mais nada depois) na pasta raiz do projeto — o mesmo nível onde está o `manage.py`. Coloque este conteúdo dentro dele:
```env
SECRET_KEY=coloque-aqui-uma-chave-secreta-qualquer
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```
💡 Dica: para gerar uma `SECRET_KEY` segura e aleatória, rode este comando:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copie o resultado e cole no lugar de `coloque-aqui-uma-chave-secreta-qualquer`.
> Esse arquivo guarda informações sensíveis e **não deve ser enviado ao GitHub** — ele já está listado no `.gitignore` do projeto, então isso é feito automaticamente.
5️⃣ Aplicar as migrações do banco de dados
As "migrações" criam as tabelas do banco de dados a partir dos modelos do Django:
```bash
python manage.py migrate
```
6️⃣ Criar um superusuário (opcional)
Se você quiser acessar o painel administrativo do Django (em `/admin/`), crie uma conta de administrador:
```bash
python manage.py createsuperuser
```
O terminal vai pedir um nome de usuário, e-mail (opcional) e senha.
7️⃣ Rodar o servidor local
Chegou a hora de ligar o projeto:
```bash
python manage.py runserver
```
Abra o navegador e acesse:
```
http://127.0.0.1:8000/
```
🎉 Pronto! O TaskFlow deve estar rodando na sua máquina.
---
📁 Estrutura do projeto
```
sistema_tarefas/
├── config/               ⚙️  Configurações principais do Django (settings, urls)
├── core/                 🏠 App inicial (redirecionamento da home)
├── usuarios/              🔐 Autenticação (login, cadastro, logout)
├── dashboard/              📊 Painel principal com estatísticas
├── tarefas/                 ✅ CRUD de tarefas (núcleo do sistema)
├── relatorios/                📈 Relatórios e resumos
├── static/                     🎨 Arquivos CSS e JavaScript
│   ├── css/
│   └── js/
├── templates/                   🖼️  Templates HTML
│   ├── components/              🧩 Sidebar, header (reutilizáveis)
│   ├── dashboard/
│   ├── tarefas/
│   ├── usuarios/
│   └── relatorios/
├── manage.py
├── requirements.txt              📦 Dependências do projeto
├── build.sh                       🏗️  Script de build usado no deploy (Render)
├── Procfile                        🚀 Comando de inicialização em produção
└── .env                             🔑 Variáveis de ambiente (não versionado)
```
---
☁️ Deploy
Este projeto está hospedado no Render, utilizando:
🖥️ Web Service rodando com Gunicorn (servidor de produção)
🗄️ Banco de dados PostgreSQL gerenciado pelo próprio Render
⚡ WhiteNoise para servir arquivos estáticos (CSS/JS) com performance
O deploy é automático: qualquer alteração enviada (`git push`) para a branch `main` dispara um novo build e atualiza o site no ar.
---
🗺️ Próximos passos
Algumas ideias e funcionalidades planejadas para o futuro do projeto:
[ ] Módulo de Projetos
[ ] Calendário integrado
[ ] Gerenciamento avançado de Usuários
[ ] Redesign visual inspirado em apps de anotações
---
📄 Licença
Este projeto é de uso pessoal/educacional.
---
<div align="center">
👤 Autor
Desenvolvido com 💙 por Rhuan
![GitHub](https://img.shields.io/badge/GitHub-PaNiiCz-181717?style=for-the-badge&logo=github&logoColor=white)
</div>