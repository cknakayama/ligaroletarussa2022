"""
Funcionalidades que acessam o Bando de Dados.
"""


import mysql.connector
from exibir_console import *


database = "rr2022"


def acesso_mysql():
    """
            Acessa o Banco de Dados.

            Retorna:    con - Conexão do Banco de Dados.
                        cursor - Método para utilizar instruções do Banco de Dados.
    """
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=database
    )
    cursor = con.cursor()
    return con, cursor


def pegar_autenticacao():
    """
            Acessa o Banco de Dados e pega o 'código de autorização'.

            Retorna:    cookie - string com o código.
    """
    con, cursor = acesso_mysql()
    cursor.execute("SELECT * FROM autenticacao")
    cookie = cursor.fetchall()
    return cookie[0][0]


def trocar_cookie():
    """
            Caso o código de autenticação não funcione, este método auxilia na troca do código.

            Para pegar o código, acesse o site do Cartola FC pelo navegador e faça o login.
            Após o login, acesse a página https://login.globo.com/api/user e copie o código apresentado
            na variável glbId.
    """
    nova_autenticacao = str(input('Digite a nova autenticação: '))
    con, cursor = acesso_mysql()
    cursor.execute(f'UPDATE autenticacao SET cookie="{nova_autenticacao}"')
    con.commit()


def nomes_colunas(tabela: str):
    """
            Acessa o Banco de Dados e pega os nomes das colunas da tabela especificada.'.

            Retorna:    lista com os nomes das colunas.
    """
    con, cursor = acesso_mysql()
    cursor.execute(f"""SELECT `COLUMN_NAME` 
                    FROM `INFORMATION_SCHEMA`.`COLUMNS` 
                    WHERE `TABLE_SCHEMA`='{database}' 
                    AND `TABLE_NAME`='{tabela}';""")
    colunas = []
    temp = cursor.fetchall()
    for coluna in temp:
        colunas.append(coluna[0])
    return colunas


def bd_dict_list(tabela: str, coluna: str, crescente=False):
    """
            Pega os dados de cada linha da tabela especificada e transforma em dicionários.

            Retorna:    lista de dicionarios.
    """
    lista_colunas = []
    colunas = nomes_colunas(tabela)
    if coluna not in colunas:
        for c in colunas:
            lista_colunas.append({f"Coluna": c})
        exibir_cabecalho("Escolha como deseja ordenar os dados:")
        listar_itens_para_escolha(lista_colunas)
        escolha = escolher_entre_opcoes(lista_colunas)
        coluna_ordem = escolha["Coluna"]
    else:
        coluna_ordem = coluna
    if crescente:
        ordem = "ASC"
    else:
        ordem = "DESC"
    lista_dados = []
    con, cursor = acesso_mysql()
    cursor.execute(f"SELECT * FROM {tabela} ORDER BY {coluna_ordem} {ordem};")
    for linha in cursor.fetchall():
        dicionario_temp = {}
        contador = 0
        for coluna in colunas:
            dicionario_temp[coluna] = linha[contador]
            contador += 1
        lista_dados.append(dicionario_temp)
    return lista_dados


def salvar_time_bd(time: dict, tabela: str):
    """
    Salva o time na tabela especificada.

    """
    valores = (time['ID'], time['Nome'], time['Cartoleiro'])
    con, cursor = acesso_mysql()
    try:
        cursor.execute(f"""INSERT INTO {tabela}(ID, Nome, Cartoleiro)
                        VALUES{valores};""")
        con.commit()
    except mysql.connector.errors.IntegrityError:
        print(f"Já existe cadastro do time {time['Nome']} com ID {time['ID']}")
    else:
        print(f"Time {time['Nome']} salvo.")


def pegar_id_times(tabela: str):
    """
    Pega os IDs da tabela especificada.
    Retorna uma lista com os Ids.
    """
    con, cursor = acesso_mysql()
    cursor.execute(f"SELECT ID FROM {tabela}")
    ids = []
    temp = cursor.fetchall()
    for i in temp:
        ids.append(i[0])
    return ids


def atualizar_pontuacao_rodada(id_time: int, rodada: int, pontos: float, tabela: str):
    """
    Salva a pontuação da Rodada especificada no time especificado.
    """
    coluna = f'Rodada{rodada}'
    colunas_atuais = nomes_colunas(tabela)
    con, cursor = acesso_mysql()
    if coluna not in colunas_atuais:
        cursor.execute(f"ALTER TABLE {tabela} ADD {coluna} double;")
        con.commit()
        print(f"Coluna {coluna} criada com sucesso.")
    cursor.execute(f"UPDATE {tabela} SET {coluna}={pontos} WHERE ID={id_time};")
    con.commit()


def atualizar_patrimonio(id_time: int, patrimonio: float, tabela: str):
    """
    Salva o patrimonio do time especificado.
    """
    coluna = 'Patrimonio'
    con, cursor = acesso_mysql()
    cursor.execute(f"UPDATE {tabela} SET {coluna}={patrimonio} WHERE ID={id_time};")
    con.commit()


def atualizar_pts_total(id_time: int, pts_rodada: float, tabela: str):
    """
    Salva a pontuação total do time especificado.
    """
    coluna = 'Pts_total'
    con, cursor = acesso_mysql()
    cursor.execute(f"SELECT {coluna} FROM {tabela} WHERE ID={id_time};")
    pts_anterior = cursor.fetchall()[0][0]
    pts_atual = pts_anterior + pts_rodada
    cursor.execute(f"UPDATE {tabela} SET {coluna}={pts_atual} WHERE ID={id_time};")
    con.commit()


def atualizar_turno_returno(id_time: int, rodada_atual: int, pts_rodada: float, tabela: str):
    """
        Salva a pontuação de turno ou returno do time especificado.
    """
    if rodada_atual <= 19:
        coluna = 'Turno'
    else:
        coluna = 'Returno'
    con, cursor = acesso_mysql()
    cursor.execute(f"SELECT {coluna} FROM {tabela} WHERE ID={id_time};")
    pts_anterior = cursor.fetchall()[0][0]
    pts_atual = pts_anterior + pts_rodada
    cursor.execute(f"UPDATE {tabela} SET {coluna}={pts_atual} WHERE ID={id_time};")
    con.commit()


def atualizar_mito(id_time: int, rodada_atual: int, pts_rodada: float, tabela: str):
    """
    Atualiza a melhor pontuação(Mito) do time especificado.
    """
    coluna1 = 'Mito'
    coluna2 = 'Mito_rodada'
    con, cursor = acesso_mysql()
    cursor.execute(f"SELECT {coluna1} FROM {tabela} WHERE ID={id_time};")
    pts_anterior = cursor.fetchall()[0][0]
    if pts_rodada > pts_anterior:
        cursor.execute(f"UPDATE {tabela} SET {coluna1}={pts_rodada}, {coluna2}={rodada_atual} WHERE ID={id_time};")
        con.commit()


def atualizar_mensal(tabela: str, rodada_atual: int):
    con, cursor = acesso_mysql()
    while True:
        print(f"Tabela: {tabela}")
        terminou_mes = str(input("Terminou o mês?[S/N] ")).strip().upper()
        if terminou_mes == "N":
            break
        elif terminou_mes == "S":
            apagar_mes = str(input("A pontuação mensal será zerada. Confirma?[S/N] ")).strip().upper()
            if apagar_mes == "S":
                cursor.execute(f"UPDATE {tabela} SET Mensal = 0;")
                con.commit()
                break
        else:
            print("Opção Inválida!")
    cursor.execute(f"SELECT ID, Mensal, Rodada{rodada_atual} FROM {tabela}")
    pontuacoes = cursor.fetchall()
    for time in pontuacoes:
        id = time[0]
        mensal = time[1] + time[2]
        cursor.execute(f"UPDATE {tabela} SET Mensal = {mensal} WHERE ID = {id};")
        con.commit()
    print(f"Pontuações Mensais da tabela {tabela} atualizadas.")


def atualizar_pontuacao_eliminatoria(id_time: int, pontos: float, tabela: str):
    """
    Salva a pontuação da Rodada no time especificado.
    """
    coluna = "Pts"
    con, cursor = acesso_mysql()
    cursor.execute(f"UPDATE {tabela} SET {coluna}={pontos} WHERE ID={id_time};")
    con.commit()


def juntar_times_cadastrados():
    tabelas = ["lprincipal_ccap", "lprincipal_scap",
               "leliminatoria_ccap", "leliminatoria_scap",
               "mmliga_ccap", "mmliga_scap"]

    for tabela in tabelas:
        times = bd_dict_list(tabela, "ID")
        for time in times:
            salvar_time_bd(time, "times_cadastrados")


def pesquisar_em_times_cadastrados():
    termo_pesquisa = str(input("Pesquisa: "))
    con, cursor = acesso_mysql()
    cursor.execute(f"SELECT * FROM times_cadastrados WHERE Nome LIKE '%{termo_pesquisa}%'")
    times = []
    for dado in cursor.fetchall():
        times.append({"ID": dado[0], "Nome": dado[1], "Cartoleiro": dado[2]})
    listar_itens_para_escolha(times)
    return escolher_entre_opcoes(times)


def listar_times_em_tabela(tabela: str):
    times = bd_dict_list(tabela, "Nome", crescente=True)
    lista = []
    for time in times:
        lista.append({"ID": time["ID"], "Nome": time["Nome"], "Cartoleiro": time["Cartoleiro"]})
    exibir_cabecalho(f"Tabela {tabela} - Times Cadastrados")
    listar_itens(lista)


def listar_tabelas_do_time(time: dict):
    tabelas = ["lprincipal_ccap", "lprincipal_scap",
               "leliminatoria_ccap", "leliminatoria_scap",
               "mmliga_ccap", "mmliga_scap"]

    exibir_cabecalho(f"Pesquisar por time {time['Nome']} no banco de dados")
    con, cursor = acesso_mysql()
    lista_tabelas = []
    for tabela in tabelas:
        cursor.execute(f"SELECT * FROM {tabela} WHERE ID={time['ID']}")
        if cursor.fetchall():
            lista_tabelas.append({"ID": time['ID'], "Nome": time['Nome'],
                                  "Cartoleiro": time['Cartoleiro'], "Tabela": tabela})
    if lista_tabelas:
        listar_itens(lista_tabelas)
    else:
        print("Time não encontrado no banco de dados.")

