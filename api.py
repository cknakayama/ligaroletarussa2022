import cartolafc
from bd import BD


class Api:
    def __init__(self):
        self.api = self.api_login()

    @staticmethod
    def api_login():
        """
                Acessa o API do Cartola FC.

                Retorna:    api - Instancia da classe API da biblioteca cartolafc.
        """
        api = cartolafc.Api()
        bd = BD()
        while True:
            try:
                api._glb_id = bd.cookie_autenticacao()
                api.liga(slug='')
            except cartolafc.CartolaFCError:
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
                    print("Nenhum time encontrado. Usuário CANCELOU a pesquisa.")
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
                    print("Nenhuma Liga encontrada. Usuário CANCELOU a pesquisa.")
                    return []
        for item in ligas:
            temp = {"nome": item.nome, "slug": item.slug}
            lista_ligas.append(temp)
        return lista_ligas

    def atualizar_nomes(self, tabela):
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