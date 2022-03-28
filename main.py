"""
Programa Principal
"""
from bd import *
from api import *
from informativos import acessar_arquivo
from exibir_console import *
from random import randint


class PontosPrincipal:
    def __init__(self):
        self.rodada = rodada() - 1
        tabelas = ["lprincipal_ccap", "lprincipal_scap"]
        atualizar_nomes_times(tabelas[0])
        self.atualizar_pontos_cc(tabelas[0])
        atualizar_nomes_times(tabelas[1])
        self.atualizar_pontos_sc(tabelas[1])

    def atualizar_pontos_cc(self, tabela: str):
        lista_times = pegar_id_times(tabela)
        for time in lista_times:
            dados = pegar_pontuacao_cc(time)
            atualizar_pontuacao_rodada(time, self.rodada, dados["Pontos"], tabela)
            atualizar_patrimonio(time, dados["Patrimonio"], tabela)
            atualizar_pts_total(time, dados["Pontos"], tabela)
            atualizar_mito(time, self.rodada, dados["Pontos"], tabela)
            atualizar_turno_returno(time, self.rodada, dados["Pontos"], tabela)

    def atualizar_pontos_sc(self, tabela: str):
        lista_times = pegar_id_times(tabela)
        for time in lista_times:
            dados = pegar_pontuacao_sc(time)
            atualizar_pontuacao_rodada(time, self.rodada, dados["Pontos"], tabela)
            atualizar_patrimonio(time, dados["Patrimonio"], tabela)
            atualizar_pts_total(time, dados["Pontos"], tabela)
            atualizar_mito(time, self.rodada, dados["Pontos"], tabela)
            atualizar_turno_returno(time, self.rodada, dados["Pontos"], tabela)


class PontosEliminatoria:
    def __init__(self):
        self.rodada = rodada() - 1
        tabelas = ["leliminatoria_ccap", "leliminatoria_scap"]
        atualizar_nomes_times(tabelas[0])
        self.atualizar_pontos_cc(tabelas[0])
        atualizar_nomes_times(tabelas[1])
        self.atualizar_pontos_sc(tabelas[1])

    @staticmethod
    def atualizar_pontos_cc(tabela: str):
        lista_times = pegar_id_times(tabela)
        for time in lista_times:
            dados = pegar_pontuacao_cc(time)
            atualizar_pontuacao_eliminatoria(time, dados["Pontos"], tabela)

    @staticmethod
    def atualizar_pontos_sc(tabela: str):
        lista_times = pegar_id_times(tabela)
        for time in lista_times:
            dados = pegar_pontuacao_sc(time)
            atualizar_pontuacao_eliminatoria(time, dados["Pontos"], tabela)


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


