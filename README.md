# wsBackend-Fabrica25.1

Este é um projeto Django para gerenciar frases e conselhos.

## Requisitos

- Python 3.8 ou superior
- Django 5.1.6
- Outros pacotes listados em `requirements.txt`

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/Raimundo-14/wsBackend-Fabrica25.1.git
    cd wsBackend-Fabrica25.1
    ```

2. Crie e ative um ambiente virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```sh
    python manage.py migrate    
    ```

## Uso

1. Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

2. Acesse o aplicativo no navegador:

    ```
    http://127.0.0.1:8000/
    ```

## Estrutura do Projeto

- `appfrase/`: Aplicativo principal que gerencia frases e conselhos.
  - `models.py`: Define o modelo `Frase`.
  - `views.py`: Contém as views para listar, editar e deletar frases.
  - `urls.py`: Define as rotas do aplicativo.
  - `templates/appfrase/`: Contém os templates HTML.
    - `home.html`: Página inicial.
    - `listar.html`: Página para listar frases.
    - `editar.html`: Página para editar uma frase.

- `frase/`: Configurações do projeto Django.
  - `settings.py`: Configurações do projeto.
  - `urls.py`: Rotas principais do projeto.
  - `wsgi.py`: Configuração WSGI para deploy.

- `manage.py`: Script de gerenciamento do Django.

## Funcionalidades

- Listar frases cadastradas.
- Adicionar novas frases.
- Editar frases existentes.
- Deletar frases.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.