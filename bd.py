"""
Funcionalidades que acessam o Bando de Dados.
"""


import mysql.connector


database = "roleta_russa_2022"


def acesso_mysql():
    """
            Acessa o Banco de Dados.

            Retorna:    con - Conecção do Banco de Dados.
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


def cookie_autenticacao():
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


def nomes_colunas(tabela:str):
    """
            Acessa o Banco de Dados e pega os nomes das colunas da tabela especificada.'.

            Retorna:    lista de tuplas com os nomes das colunas.
    """
    con, cursor = acesso_mysql()
    cursor.execute(f"""SELECT `COLUMN_NAME` 
                    FROM `INFORMATION_SCHEMA`.`COLUMNS` 
                    WHERE `TABLE_SCHEMA`='roleta_russa_2022' 
                    AND `TABLE_NAME`='{tabela}';""")
    return cursor.fetchall()


def bd_dict_list(tabela:str):
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
            dicionario_temp[f"{coluna[0]}"] = linha[contador]
            contador += 1
        lista_dados.append(dicionario_temp)
    return lista_dados


def dict_list_bd(lista:list, tabela:str):
    con, cursor = acesso_mysql()
    if not tabela:
        print("Tabela não informada!")
        nome_tabela = str(input("Digite o nome da nova tabela que será criada: "))


