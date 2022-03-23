"""
Programa Principal
"""
from bd import *
from api import *
from exibir_console import *


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


class CadastrarTime():
    def __init__(self, time: dict, tabelas: list):
        if len(tabelas) > 0:
            for tabela in tabelas:
                salvar_time_bd(time, tabela)
        else:
            print("Nenhuma tabela informada.")
