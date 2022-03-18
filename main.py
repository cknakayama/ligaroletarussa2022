"""
Programa Principal
"""
from bd import salvar_time_bd, atualizar_pontuacao_rodada, pegar_id_times, atualizar_patrimonio
from api import rodada, atualizar_nomes_times, pegar_pontuacao_cc, pegar_pontuacao_sc
from exibir_console import *


class PrincipalCC:
    def __init__(self):
        self.tabela = "lprincipal_ccap"
        atualizar_nomes_times(self.tabela)
        self.rodada = rodada() - 1
        self.lista_times = pegar_id_times(self.tabela)
        self.atualizar_pontos()

    def atualizar_pontos(self):
        for time in self.lista_times:
            dados = pegar_pontuacao_cc(time)
            atualizar_pontuacao_rodada(time, self.rodada, dados["Pontos"], self.tabela)
            atualizar_patrimonio(time, dados["Patrimonio"], self.tabela)

    def atualizar_pts_total(self):
        pass

