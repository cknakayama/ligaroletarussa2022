"""
Funcionalidades para exibir os menus da interface(console).
"""

import os
from roleta_russa import *
from exibir_console import *
from time import sleep


def menu_principal():
    """
    Método que exibe o menu principal no terminal.
    O usuário pode escolher entre as opções ou sair do programa.

    Retorna:    escolha - retorna uma string com a escolha do usuário.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_inicial = [{'opção': 'Cadastrar time'},
                    {'opção': 'Atualizar informativos'},
                    {'opção': 'Novo Mata-mata da Liga'}]
    while True:
        exibir_cabecalho('Menu Principal')
        listar_itens_para_escolha(menu_inicial)
        escolha = escolher_entre_opcoes(menu_inicial)
        if not escolha:
            terminar_programa()
        elif escolha["opção"] == "Cadastrar time":
            cadastrar_time()
        elif escolha["opção"] == "Atualizar informativos":
            atualizar_informativos()
        elif escolha["opção"] == "Novo Mata-mata da Liga":
            matamata_liga()


def cadastrar_time():
    os.system('cls' if os.name == 'nt' else 'clear')
    menu = [{'opção': 'Cadastrar time individual'},
            {'opção': 'Cadastrar times de uma liga'},
            {'opção': 'Cadastrar times cadastrado em uma liga'}]

    lista_tabelas = [{'opção': 'Liga Principal com Capitão', 'tabela': 'lprincipal_ccap'},
                     {'opção': 'Liga Principal sem Capitão', 'tabela': 'lprincipal_scap'},
                     {'opção': 'Liga Eliminatória com Capitão', 'tabela': 'leliminatoria_ccap'},
                     {'opção': 'Liga Eliminatória sem Capitão', 'tabela': 'leliminatoria_scap'}]

    exibir_cabecalho("Cadastro de Times")
    listar_itens_para_escolha(menu)
    escolha_menu = escolher_entre_opcoes(menu)
    if not escolha_menu:
        print("Voltando ao Menu Principal...")
        sleep(2)
        menu_principal()
    elif escolha_menu["opção"] == 'Cadastrar time individual':
        while True:
            time = pesquisar_time()
            if not time:
                print("Voltando ao Menu Principal...")
                sleep(2)
                menu_principal()
            else:
                print("Onde deseja cadastrar o time?")
                listar_itens_para_escolha(lista_tabelas)
                escolha_tabela = escolher_varias_opcoes(lista_tabelas)
                if not escolha_tabela:
                    print("Voltando ao Menu Principal...")
                    sleep(2)
                    menu_principal()
                else:
                    tabelas = []
                    for tabela in escolha_tabela:
                        tabelas.append(tabela['tabela'])
                    CadastrarTime(time, tabelas)
            continuar = str(input("Deseja Cadastrar mais times? [S/N] ")).strip().upper()
            if continuar == "N":
                print("Voltando ao Menu Principal...")
                sleep(2)
                menu_principal()
            elif continuar == "S":
                continue
            else:
                print("Opção inválida!")
    elif escolha_menu["opção"] == 'Cadastrar times cadastrado em uma liga':
        cadastrar_times_na_liga()
        print("Voltando ao Menu Principal...")
        sleep(2)
        menu_principal()
    else:
        liga = pesquisar_liga()
        times = times_liga(liga['Slug'])
        if not times:
            print("Nenhum time encontrado.")
            print("Voltando ao Menu Principal...")
            sleep(2)
            menu_principal()
        else:
            print("Onde deseja cadastrar os times?")
            listar_itens_para_escolha(lista_tabelas)
            escolha_tabela = escolher_entre_opcoes(lista_tabelas)
            if not escolha_tabela:
                print("Voltando ao Menu Principal...")
                sleep(2)
                menu_principal()
            else:
                tabela = [escolha_tabela['tabela']]
                for time in times:
                    CadastrarTime(time, tabela)
                    print(f"Time {time['Nome']} Cadastrado na tabela {escolha_tabela['tabela']}")
        print("Voltando ao Menu Principal...")
        sleep(2)
        menu_principal()


def atualizar_informativos():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_cabecalho("Informativos")
    print("Atualizando pontuação dos times...")
    Principal()
    Eliminatoria()
    mm = MataMataLiga()
    mm.atualizar_pontuacao()
    print("Informativos atualizados...")
    sleep(1)
    print("Voltando ao Menu Principal...")
    sleep(2)
    menu_principal()


def matamata_liga():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_cabecalho("Novo Mata-mata da liga")
        print("Ao criar um novo mata-mata, o antigo será apagado!")
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
        if continuar == "N":
            print("Voltando ao Menu Principal...")
            sleep(2)
            menu_principal()
        elif continuar == "S":
            mm = MataMataLiga()
            mm.atualizar_participantes()
            mm.sorteio()
            print("Mata-mata das Ligas Principais criados com sucesso.")
            print("Voltando ao Menu Principal...")
            sleep(2)
            menu_principal()
        else:
            print("Opção inválida!")


def cadastrar_times_na_liga():
    lista_tabelas = [{'opção': 'Liga Principal com Capitão', 'tabela': 'lprincipal_ccap'},
                     {'opção': 'Liga Principal sem Capitão', 'tabela': 'lprincipal_scap'},
                     {'opção': 'Liga Eliminatória com Capitão', 'tabela': 'leliminatoria_ccap'},
                     {'opção': 'Liga Eliminatória sem Capitão', 'tabela': 'leliminatoria_scap'},
                     {'opção': 'Mata-Mata Avulso', 'tabela': 'mmavulso'}]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_cabecalho("Cadastrar times em uma Liga")
        print("Escolher na lista de cadastro os times para inserir na liga.")
        print("Escolha em qual liga deseja cadastrar o(s) time(s):")
        listar_itens_para_escolha(lista_tabelas)
        escolha_tabela = escolher_varias_opcoes(lista_tabelas)
        times = bd_dict_list("times_cadastrados", coluna="Nome", crescente=True)
        for tabela in escolha_tabela:
            for time in times:
                os.system('cls' if os.name == 'nt' else 'clear')
                exibir_cabecalho("Cadastrar times em uma Liga")
                exibir_cabecalho(f"Tabela: {tabela['opção']}")
                print(f"{time['ID']}  -  {time['Nome']}  -  {time['Cartoleiro']}")
                escolha = str(input("Deseja cadastrar o time?[S/N] ")).strip().upper()
                if escolha == "S":
                    CadastrarTime(time, [tabela['tabela']])


menu_principal()
