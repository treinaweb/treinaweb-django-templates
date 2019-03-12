from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    nome_da_empresa = "TreinaWeb"
    descricao_da_empresa = "Há mais de 12 anos formando desenvolvedores de ponta! São mais de 4.000 horas de conteúdo, com formações completas e com foco no mercado de trabalho."

    contato_empresa = {
        "endereco": "Av. Paulista, 1765, Conj 71 e 72 - Bela Vista - São Paulo - SP",
        "telefone": "111222333",
        "email": "contato@treinaweb.com.br"
    }

    cursos_home = {
        "1": {"titulo": "Django Fundamentos", "descricao": "Aprenda toda a base do Django agora mesmo!!"},
        "2": {"titulo": "Flask Fundamentos", "descricao": "Aprenda toda a base do Flask agora mesmo!!"},
        "3": {"titulo": "Python OO", "descricao": "Aprenda a orientação à objetos com Python agora mesmo!!"},
    }

    return render(request, 'empresa/index.html', {'nome_empresa':nome_da_empresa, 'descricao_empresa':descricao_da_empresa,
                                                  'contato_empresa': contato_empresa, 'cursos_home':cursos_home})

def about(request):
    return HttpResponse("Página sobre")

def contact(request, id):
    return HttpResponse(id)