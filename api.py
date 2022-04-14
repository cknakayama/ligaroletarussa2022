"""
Funcionalidades que acessam a APi do CartolaFC.
"""

import cartolafc
from mysqlx import OperationalError
from bd import *
from exibir_console import *
import requests


def api_login():
    """
            Acessa o API do Cartola FC.

            Retorna:    api - Instancia da classe API da biblioteca cartolafc.
    """
    api = cartolafc.Api()
    while True:
        try:
            api._glb_id = pegar_autenticacao()
            api.liga(slug='roleta-ru-a')
        except cartolafc.CartolaFCError:
            print("Erro de login.")
            trocar_cookie()
        else:
            break
    return api


def rodada():
    """
    Pega o número da rodada atual.

    Retorna:    status['rodada_atual'] - inteiro representando a rodada atual.
    """
    try:
        url_1 = 'https://api.cartolafc.globo.com/mercado/status'
        r = requests.get(url=url_1)
        status = r.json()
    except:
        print('Não foi possível pegar a rodada no sistema.')
        return int_input('Digite a rodada:')
    else:
        return status['rodada_atual']


def pesquisar_time():
    """
            Pesquisa por um time na API do CArtola FC.

            Retorna:    Dicionário com os dados do time escolhido ou dicionario vazio.
    """
    api = api_login()
    lista_times = []
    while True:
        while True:
            termo_pesquisa = str(input('Digite o nome do Time: ')).strip()
            times = api.times(query=termo_pesquisa)
            if times:
                break
            else:
                continuar = str(input('Time não encontrado. Gostaria de tentar novamente?[S/N] ')).strip().upper()
                if continuar == "N":
                    print("Nenhum time encontrado. Usuário CANCELOU a pesquisa.")
                    return {}
        for item in times:
            temp = {"ID": item.id, "Nome": item.nome, "Cartoleiro": item.nome_cartola}
            lista_times.append(temp)
        listar_itens_para_escolha(lista_times)
        escolha = escolher_entre_opcoes(lista_times)
        if escolha:
            break
        else:
            continuar = str(input('Gostaria de tentar novamente?[S/N] ')).strip().upper()
            if continuar == "N":
                print("Usuário CANCELOU a pesquisa.")
                return {}
    return escolha


def pesquisar_liga():
    """
    Pesquisa por uma liga na API do CArtola FC.

    Retorna:    Dicionário com os dados da Liga
    """
    api = api_login()
    lista_ligas = []
    while True:
        termo_pesquisa = str(input('Digite o nome da Liga: ')).strip()
        ligas = api.ligas(query=termo_pesquisa)
        if ligas:
            break
        else:
            continuar = str(input('Liga não encontrado. Gostaria de tentar novamente?[S/N] ')).strip().upper()
            if continuar == "N":
                print("Nenhuma Liga encontrada. Usuário CANCELOU a pesquisa.")
                terminar_programa()
    for item in ligas:
        temp = {"Nome": item.nome, "Slug": item.slug}
        lista_ligas.append(temp)
    listar_itens_para_escolha(lista_ligas)
    return escolher_entre_opcoes(lista_ligas)


def atualizar_nomes_times(tabela: str):
    api = api_login()
    con, cursor = acesso_mysql()
    try:
        cursor.execute(f"SELECT ID FROM {tabela};")
        times = cursor.fetchall()
        for t in times:
            id_time = t[0]
            time = api.time(id=id_time, as_json=True)
            atual = {'nome': time['time']['nome'], 'cartoleiro': time['time']['nome_cartola']}
            cursor.execute(
                f'UPDATE {tabela} SET Nome="{atual["nome"]}", Cartoleiro="{atual["cartoleiro"]}" WHERE ID={id_time};')
            con.commit()
    except OperationalError:
        print(f'Tabela {tabela} ou Colunas ID, Nome e Cartoleiro inexistentes.')
    except cartolafc.errors.CartolaFCError:
        print("Time ainda não foi escalado na temporada.")
    else:
        print(f"Nomes dos times da tabela {tabela} foram atualizados.")


def times_liga(slug: str):
    """
        Pega todos os times da liga especificada.

        Retorna:    lista com os times da liga.
    """
    api = api_login()
    times = api.liga(slug=slug).times
    lista_times = []
    for time in times:
        dicionario = {"ID": time.id, "Nome": time.nome, "Cartoleiro": time.nome_cartola}
        lista_times.append(dicionario)
    return lista_times


def pegar_pontuacao_cc(id_time: int):
    api = api_login()
    try:
        t = api.time(id=id_time, as_json=True)
    except cartolafc.CartolaFCError:
        return {'ID': id_time, 'Pontos': 0, 'Patrimonio': 0}
    else:
        if not t['pontos']:
            t['pontos'] = 0
        return {'ID': id_time, 'Pontos': t['pontos'], 'Patrimonio': t['patrimonio']}


def pegar_pontuacao_sc(id_time: int):
    api = api_login()
    try:
        time = api.time(id=id_time, as_json=True)
    except cartolafc.CartolaFCError:
        return {'ID': id_time, 'Pontos': 0, 'Patrimonio': 0}
    else:
        pontos = 0
        for jogadores in time['atletas']:
            pontos += jogadores['pontos_num']
        return {'ID': id_time, 'Pontos': pontos, 'Patrimonio': time['patrimonio']}
