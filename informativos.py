"""
Funcionalidades para atualizar os informativos
"""
import openpyxl
from bd import *
from api import rodada


path = "informativos.xlsx"


def acessar_arquivo(planilha: str):
    arquivo = openpyxl.load_workbook(path)
    return arquivo, arquivo[planilha]


def informativos_top10():
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        nome = "D"
        pts = "X"
        inicio = 8
        passo = 2
        contagem = 0
        maximo = 10
        arquivo, planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Pts_total")
        while contagem < maximo:
            planilha[f'{nome}{inicio}'] = times[contagem]['Nome']
            planilha[f'{pts}{inicio}'] = times[contagem]['Pts_total']
            inicio += passo
            contagem += 1
        arquivo.save(path)


def informativos_turno():
    nome = "AG"
    pts = "BA"
    inicio = 8
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        arquivo, planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Turno")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Turno']
        arquivo.save(path)


def informativos_returno():
    nome = "AG"
    pts = "BA"
    inicio = 20
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        arquivo, planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Returno")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Returno']
        arquivo.save(path)


def informativos_patrimonio():
    nome = "AG"
    pts = "BA"
    inicio = 32
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        arquivo, planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Patrimonio")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Patrimonio']
        arquivo.save(path)


def informativos_mito():
    nome = "AG"
    pts = "BA"
    rodada = "BG"
    inicio = 44
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        arquivo, planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Mito")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Mito']
            planilha[f'{rodada}{num}'] = times[t]['Mito_rodada']
        arquivo.save(path)


def verificar_mes():
    meses = [{'mes': 'Abril', 'numero': 4}, {'mes': 'Maio', 'numero': 5}, {'mes': 'Junho', 'numero': 6},
             {'mes': 'Julho', 'numero': 7}, {'mes': 'Agosto', 'numero': 8}, {'mes': 'Setembro', 'numero': 9},
             {'mes': 'Outubro', 'numero': 10}, {'mes': 'Novembro', 'numero': 11}, ]

    listar_itens(meses)
    escolha = escolher_entre_opcoes(meses)
    return escolha['numero']



def informativos_mensal(mes: int):
    nome = "BM"
    pts = "CG"
    inicio = 6 + ((mes - 4) * 4)
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        arquivo, planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Mensal")
        planilha[f'{nome}{inicio}'] = times[0]['Nome']
        planilha[f'{pts}{inicio}'] = times[0]['Mensal']
        arquivo.save(path)


def informativos_eliminatoria():
    nome = "C"
    pts = "W"
    inicio = 3
    tabelas = ["leliminatoria_ccap", "leliminatoria_scap"]
    for tab in tabelas:
        arquivo, planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Pts")
        contador = 0
        for t in times:
            num = inicio + contador
            planilha[f'{nome}{num}'] = t['Nome']
            planilha[f'{pts}{num}'] = t['Pts']
            contador += 2
        arquivo.save(path)

