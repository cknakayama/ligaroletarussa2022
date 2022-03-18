"""
Funcionalidades que acessam o Bando de Dados.
"""


import mysql.connector


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


def bd_dict_list(tabela: str):
    """
            Pega os dados de cada linha da tabela especificada e transforma em dicionários.

            Retorna:    lista de dicionarios.
    """
    lista_dados = []
    con, cursor = acesso_mysql()
    colunas = nomes_colunas(tabela)
    cursor.execute(f"SELECT * FROM {tabela}")
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
        print(f"Já existe cadastro do time com ID {time['ID']}")
    else:
        print("Time salvo")


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
    else:
        print(f"Coluna {coluna} já existe.")
    cursor.execute(f"UPDATE {tabela} SET {coluna}={pontos} WHERE ID={id_time};")
    con.commit()
    print("Pontuação salva com sucesso.")


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
