import cartolafc
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


class Api:
    def __init__(self):
        self.api = self.api_login()

    def api_login(self):
        """
                Acessa o API do Cartola FC.

                Retorna:    api - Instancia da classe API da biblioteca cartolafc.
        """
        api = cartolafc.Api()
        bd = BD()
        while True:
            try:
                api._glb_id = bd.cookie_autenticacao()
                api.ligas(query='')
            except:
                print("Erro de login.")
                bd.trocar_cookie()
            else:
                break
        return api

    def pesquisar_time(self):
        """
                Pesquisa por um time na API do CArtola FC.

                Recebe:     termo_pesquisa(opcional) - termo que será utilizado para efetuar a pesquisa.

                Retorna:    lista_times - uma lista de dicionários contendo os dados dos times escontrados ou
                                            uma lista vazia caso o usuário desista de pesquisar.
        """
        lista_times = []
        while True:
            termo_pesquisa = str(input('Digite o nome do Time: ')).strip()
            times = self.api.times(query=termo_pesquisa)
            if times:
                break
            else:
                continuar = str(input('Time não encontrado. Gostaria de tentar novamente?[S/N] ')).strip().upper()
                if continuar == "N":
                    print("Nenhum time selecionado.")
                    return []
        for item in times:
            temp = {"id": item.id, "nome": item.nome, "cartoleiro": item.nome_cartola}
            lista_times.append(temp)
        return lista_times

    def pesquisar_liga(self):
        """
        Pesquisa por uma liga na API do CArtola FC.

        Recebe:     termo_pesquisa(opcional) - termo que será utilizado para efetuar a pesquisa.

        Retorna:    lista_ligas - uma lista de dicionários contendo os dados das ligas encontradas ou
                                    uma lista vazia caso o usuário desista da procura.
        """
        lista_ligas = []
        while True:
            termo_pesquisa = str(input('Digite o nome da Liga: ')).strip()
            ligas = self.api.ligas(query=termo_pesquisa)
            if ligas:
                break
            else:
                continuar = str(input('Liga não encontrado. Gostaria de tentar novamente?[S/N] ')).strip().upper()
                if continuar == "N":
                    print("Nenhuma Liga selecionada.")
                    return []
        for item in ligas:
            temp = {"nome": item.nome, "slug": item.slug}
            lista_ligas.append(temp)
        return lista_ligas

