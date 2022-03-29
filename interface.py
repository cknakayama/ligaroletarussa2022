"""
Funcionalidades para exibir os menus da interface(console).
"""

from os import system
from bd import *
from roleta_russa import *
from exibir_console import *


def sair():
    system('cls') or None
    print('Saindo do Programa')
    exit()


def menu_principal():
    """
    Método que exibe o menu principal no terminal.
    O usuário pode escolher entre as opções ou sair do programa.

    Retorna:    escolha - retorna uma string com a escolha do usuário.
    """
    menu_inicial = [{'opção': 'Cadastrar time'},
                    {'opção': 'Atualizar informativos'},
                    {'opção': 'Criar Mata-matas da Liga'},
                    {'opção': 'Atualizar Pontuação dos Mata-matas da Liga'}]
    while True:
        exibir_cabecalho('Menu Principal')
        listar_itens(menu_inicial)
        escolha = escolher_entre_opcoes(menu_inicial)
        if not escolha:
            sair()
        else:
            return escolha


def cadastrar_time():
    menu = [{'opção': 'Cadastrar time individual'},
            {'opção': 'Cadastrar times de uma liga'}]

    lista_tabelas = [{'opção': 'Liga Principal com Capitão', 'tabela': 'lprincipal_ccap'},
                     {'opção': 'Liga Principal sem Capitão', 'tabela': 'lprincipal_ccap'},
                     {'opção': 'Liga Eliminatória com Capitão', 'tabela': 'leliminatoria_ccap'},
                     {'opção': 'Liga Eliminatória sem Capitão', 'tabela': 'leliminatoria_ccap'}]

    exibir_cabecalho("Cadastro de Times")
    listar_itens(menu)
    escolha_menu = escolher_entre_opcoes(menu)
    if not escolha_menu:
        sair()
    elif escolha_menu == 'Cadastrar time individual':
        time = pesquisar_time()
        if not time:
            sair()
        else:
            print("Onde deseja cadastrar o time?")
            listar_itens(lista_tabelas)
            escolha_tabela = escolher_varias_opcoes(lista_tabelas)
            if not escolha_tabela:
                sair()
            else:
                tabelas = []
                for tabela in escolha_tabela:
                    tabelas.append(tabela['tabela'])
                CadastrarTime(time, tabelas)
    else:
        liga = pesquisar_liga()
        times = times_liga(liga['Slug'])
        if not times:
            print("Nenhum time encontrado.")
            sair()
        else:
            print("Onde deseja cadastrar os times?")
            listar_itens(lista_tabelas)
            escolha_tabela = escolher_entre_opcoes(lista_tabelas)
            if not escolha_tabela:
                sair()
            else:
                for time in times:
                    CadastrarTime(time, escolha_tabela['tabela'])
                    print(f"Time {time['Nome']} Cadastrado na tabela {escolha_tabela['tabela']}")


def atualizar_informativos():
    print("Atualizando pontuação dos times...")
    Principal()
    Eliminatoria()


