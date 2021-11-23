"""
Funcionalidades que acessam a APi do CartolaFC.
"""

import cartolafc
from bd import *


def api_login():
    """
            Acessa o API do Cartola FC.

            Retorna:    api - Instancia da classe API da biblioteca cartolafc.
    """
    api = cartolafc.Api()
    while True:
        try:
            api._glb_id = cookie_autenticacao()
            api.liga(slug='roleta-ru-a')
        except cartolafc.CartolaFCError:
            print("Erro de login.")
            trocar_cookie()
        else:
            break
    return api

def pesquisar_time():
    """
            Pesquisa por um time na API do CArtola FC.

            Retorna:    lista_times - uma lista de dicionários contendo os dados dos times escontrados ou
                                        uma lista vazia caso o usuário desista de pesquisar.
    """
    api = api_login()
    lista_times = []
    while True:
        termo_pesquisa = str(input('Digite o nome do Time: ')).strip()
        times = api.times(query=termo_pesquisa)
        if times:
            break
        else:
            continuar = str(input('Time não encontrado. Gostaria de tentar novamente?[S/N] ')).strip().upper()
            if continuar == "N":
                print("Nenhum time encontrado. Usuário CANCELOU a pesquisa.")
                return []
    for item in times:
        temp = {"id": item.id, "nome": item.nome, "cartoleiro": item.nome_cartola}
        lista_times.append(temp)
    return lista_times

def pesquisar_liga():
    """
    Pesquisa por uma liga na API do CArtola FC.

    Retorna:    lista_ligas - uma lista de dicionários contendo os dados das ligas encontradas ou
                                uma lista vazia caso o usuário desista da procura.
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
                return []
    for item in ligas:
        temp = {"nome": item.nome, "slug": item.slug}
        lista_ligas.append(temp)
    return lista_ligas

def atualizar_nomes(tabela):
    pass
    """api = self.acesso_autenticado()
    con, cursor = self.acessar_banco_de_dados()
    while True:
        try:
            cursor.execute(f"SELECT ID, Nome, Cartoleiro FROM {tabela}")
        except OperationalError:
            print(f'Tabela {tabela} ou Colunas ID, Nome e Cartoleiro inexistentes.')
            continue
        else:
            times = cursor.fetchall()
            break
    for t in times:
        id = t[0]
        time = api.time(id=id, as_json=True)
        atual = {'nome': time['time']['nome'], 'cartoleiro': time['time']['nome_cartola']}
        cursor.execute(
            f'UPDATE {tabela} SET Nome="{atual["nome"]}", Cartoleiro="{atual["cartoleiro"]}" WHERE ID={id}')
        con.commit()"""


def times_liga(slug:str):
    """
        Pega todosos times da liga especificada.

        Retorna:    lista com os times da liga.
    """
    api = api_login()
    times = api.liga(slug=slug).times
    lista_times = []
    for time in times:
        dicionario = {"id": time.id, "nome": time.nome, "cartoleiro": time.nome_cartola}
        lista_times.append(dicionario)
    return lista_times
