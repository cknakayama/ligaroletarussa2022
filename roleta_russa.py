"""
Programa Principal
"""

from api import *
from informativos import *
from exibir_console import *
from random import randint


class Principal:
    def __init__(self):
        self.rodada = rodada() - 1
        tabelas = ["lprincipal_ccap", "lprincipal_scap"]
        for tabela in tabelas:
            atualizar_nomes_times(tabela)
            self.atualizar_pontos(tabela)
            print(f"Tabela {tabela} atualizada com a rodada {self.rodada}.")

    def atualizar_pontos(self, tabela: str):
        print(f"Atualizando tabela {tabela}")
        lista_times = pegar_id_times(tabela)
        for time in lista_times:
            if tabela == "lprincipal_ccap":
                dados = pegar_pontuacao_cc(time)
            else:
                dados = pegar_pontuacao_sc(time)
#            print(f"Pontuação do time {time} foi acessada.")
            atualizar_pontuacao_rodada(time, self.rodada, dados["Pontos"], tabela)
#            print(f"Pontuação do time {time} atualizada.")
            atualizar_patrimonio(time, dados["Patrimonio"], tabela)
#            print(f"Patrimonio do time {time} atualizada.")
            atualizar_pts_total(time, dados["Pontos"], tabela)
#            print(f"Pts_total do time {time} atualizada.")
            atualizar_mito(time, self.rodada, dados["Pontos"], tabela)
#            print(f"Mito do time {time} atualizada.")
            atualizar_turno_returno(time, self.rodada, dados["Pontos"], tabela)
#            print(f"Turno do time {time} atualizada.")
        atualizar_mensal(tabela, self.rodada)


class Eliminatoria:
    def __init__(self):
        self.rodada = rodada() - 1
        tabelas = ["leliminatoria_ccap", "leliminatoria_scap"]
        for tabela in tabelas:
            print(f"Tabela: {tabela}")
            atualizar_nomes_times(tabela)
            self.atualizar_pontos(tabela)
            print(f"Tabela {tabela} atualizada com a rodada {self.rodada}.")
            self.eliminacao(tabela)

    @staticmethod
    def atualizar_pontos(tabela: str):
        lista_times = pegar_id_times(tabela)
        for time in lista_times:
            if tabela == "leliminatoria_ccap":
                dados = pegar_pontuacao_cc(time)
            else:
                dados = pegar_pontuacao_sc(time)
            atualizar_pontuacao_eliminatoria(time, dados["Pontos"], tabela)

    def eliminacao(self, tabela: str):
        eliminar = [
            {"rodada_inicio": 5, "rodada_final": 10, "num_eliminados": 2}
        ]

        num_eliminados = 0
        for esquema in eliminar:
            if esquema["rodada_inicio"] <= self.rodada <= esquema["rodada_final"]:
                num_eliminados = esquema["num_eliminados"]
        if num_eliminados != 0:
            times = bd_dict_list(tabela, "Pts")
            times_eliminados = times[-int(num_eliminados):]
            print("Os seguintes times serão eliminados:")
            listar_itens_para_escolha(times_eliminados)
            while True:
                eliminar = str(input("Confirma?[S/N] ")).strip().upper()
                if eliminar == "N":
                    print("Os Times não foram Eliminados.")
                    break
                elif eliminar == "S":
                    con, cursor = acesso_mysql()
                    for time in times_eliminados:
                        id = time["ID"]
                        cursor.execute(f"DELETE FROM {tabela} WHERE ID={id}")
                        con.commit()
                        print(f"{time['Nome']} - Cartoleiro: {time['Cartoleiro']} foi Eliminado.")
                    break
                else:
                    print("Opção Inválida.")
        else:
            print("Nenhum time será eliminado nessa rodada.")


class CadastrarTime:
    def __init__(self, time: dict, tabelas: list):
        if len(tabelas) > 0:
            for tabela in tabelas:
                salvar_time_bd(time, tabela)
        else:
            print("Nenhuma tabela informada.")


class MataMataLiga:
    def __init__(self):
        self.coluna = f'Rodada{rodada() - 1}'
        self.origem = ["lprincipal_ccap", "lprincipal_scap"]
        self.destino = ["mmliga_ccap", "mmliga_scap"]

    def atualizar_participantes(self):
        for c in range(0, 2):
            times = bd_dict_list(tabela=self.origem[c], coluna=self.coluna)
            for t in range(0, 64):
                time = times[t]
                salvar_time_bd(time=time, tabela=self.destino[c])

    def salvar_chaveamento(self, planilha: str, times: list):
        plan = acessar_arquivo(planilha)
        localizacao = [{"Chave": 1, "Lado": "Impar", "ID": "A", "Nome": "B"},
                       {"Chave": 1, "Lado": "Par", "ID": "O", "Nome": "J"},
                       {"Chave": 2, "Lado": "Impar", "ID": "Q", "Nome": "R"},
                       {"Chave": 2, "Lado": "Par", "ID": "Y", "Nome": "Z"}]
        num = 5
        contador = 0
        for time in times:
            if contador < 32:
                if (contador + 1) % 2 == 0:
                    local = localizacao[1]
                else:
                    local = localizacao[0]
            else:
                if (contador + 1) % 2 == 0:
                    local = localizacao[3]
                else:
                    local = localizacao[2]
            plan[f'{local["ID"]}{num}'] = time["ID"]
            plan[f'{local["Nome"]}{num}'] = time["Nome"]
            num += 2
            contador += 1

    def sorteio(self):
        for c in range(0, 2):
            times = bd_dict_list(tabela=self.destino[c], coluna="ID")
            sorteio = []
            valores = []
            while len(sorteio) != len(times):
                while True:
                    numero = randint(0, 63)
                    if numero not in valores:
                        valores.append(numero)
                        break
                sorteio.append(times[numero])
            self.salvar_chaveamento(planilha=self.destino[c], times=sorteio)

    def atualizar_pontuacao(self):
        for planilha in self.destino:
            plan = acessar_arquivo(planilha)
            localizacao = [{"ID": "A", "Pts": "G"},
                           {"ID": "O", "Pts": "I"},
                           {"ID": "Q", "Pts": "W"},
                           {"ID": "Y", "Pts": "Y"}]
            for local in localizacao:
                num = 5
                while True:
                    id = plan[f'{local["ID"]}{num}'].value
                    if id:
                        if planilha == "mmliga_ccap":
                            pontos = pegar_pontuacao_cc(id_time=id)
                        else:
                            pontos = pegar_pontuacao_sc(id_time=id)
                    else:
                        break
                    plan[f'{local["Pts"]}{num}'] = pontos["Pontos"]
                    num += 2
        print("Pontuação dos confrontos do Mata-mata da Liga foram atualizadas.")


