import mysql.connector


class BD:
    def __init__(self):
        self.database = "roleta_russa_2022"

    def acesso_mysql(self):
        """
                Acessa o Banco de Dados.

                Retorna:    con - Conecção do Banco de Dados.
                            cursor - Método para utilizar instruções do Banco de Dados.
        """
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=self.database
        )
        cursor = con.cursor()
        return con, cursor

    def cookie_autenticacao(self):
        """
                Acessa o Banco de Dados e pega o 'código de autorização'.

                Retorna:    cookie - string com o código.
        """
        con, cursor = self.acesso_mysql()
        cursor.execute("SELECT * FROM autenticacao")
        cookie = cursor.fetchall()
        return cookie[0][0]

    def trocar_cookie(self):
        """
                Caso o código de autenticação não funcione, este método auxilia na troca do código.

                Para pegar o código, acesse o site do Cartola FC pelo navegador e faça o login.
                Após o login, acesse a página https://login.globo.com/api/user e copie o código apresentado
                na variável glbId.
        """
        nova_autenticacao = str(input('Digite a nova autenticação: '))
        con, cursor = self.acesso_mysql()
        cursor.execute(f'UPDATE autenticacao SET cookie={nova_autenticacao}')
        con.commit()
