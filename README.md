<p align="center">
  <a href="https://www.grupojacto.com.br/" target="blank"><img src="https://yt3.googleusercontent.com/A1ZKD7DaizCjDtbJ83-f9c0A9rcokgR0GOlMhg9LK5vljUc4X2qEGO19m9D90tz3sIAbFuQIaQ=s900-c-k-c0x00ffffff-no-rj" width="250" alt="Grupo Jacto Logo" /></a>
</p>

# Estágio: Case - Grupo Jacto | [Documentação](https://github.com/stevalves/m6sp2-back/blob/main/DOC.md)


Esta aplicação foi desenvolvida como parte do processo seletivo do Grupo Jacto, ela consiste em uma API simples cujo propósito é criar, listar, editar e remover carros de um banco de dados.

## **Tecnologias e bibliotecas**:
* Python
* Django
* DRF

###

Crie seu ambiente virtual:

```bash
# shell
python -m venv venv
```

Ative seu ambiente virutal:

```bash
# linux
source venv/bin/activate

# windows
.\venv\Scripts\activate

# git bash
source venv/Scripts/activate
```

## Instalação

Instalação das bibliotecas necessárias para rodar o projeto:

```bash
# shell
pip install -r requirements.txt
```
## Migração Banco de dados

Por padrão o projeto ira gerar um sqlite3 nos arquivos do projeto:

```bash
# shell
python manage.py migrate
```
## Rodar o servidor

Por padrão o projeto ira gerar um sqlite3 nos arquivos do projeto:

```bash
# shell
python manage.py runserver {port}
```

<p align="center">Obrigado pela atenção! <a href="https://owl-tau.vercel.app/" target="blank">Mais dos meus projetos</a></p> 
