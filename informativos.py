"""
Funcionalidades para atualizar os informativos
"""
import openpyxl
from bd import bd_dict_list
from api import rodada


path = "informativos.xlsx"


def acessar_arquivo(planilha: str):
    arquivo = openpyxl.load_workbook(path)
    return arquivo[planilha]


def informativos_top10():
    nome = "D"
    pts = "X"
    inicio = 8
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Pts_Total")
        for t in range(0, 19, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Pts_Total']


def informativos_turno():
    nome = "AG"
    pts = "BA"
    inicio = 8
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Turno")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Turno']


def informativos_returno():
    nome = "AG"
    pts = "BA"
    inicio = 20
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Returno")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Returno']


def informativos_patrimonio():
    nome = "AG"
    pts = "BA"
    inicio = 32
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Patrimonio")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Patrimonio']


def informativos_mito():
    nome = "AG"
    pts = "BA"
    rodada = "BG"
    inicio = 44
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Mito")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Mito']
            planilha[f'{rodada}{num}'] = times[t]['Mito_rodada']


def informativos_mensal(mes: int):
    nome = "BM"
    pts = "CG"
    inicio = 6 + ((mes - 4) * 4)
    tabelas = ["lprincipal_ccap", "lprincipal_scap"]
    for tab in tabelas:
        planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Mensal")
        for t in range(0, 5, 2):
            num = inicio + t
            planilha[f'{nome}{num}'] = times[t]['Nome']
            planilha[f'{pts}{num}'] = times[t]['Mensal']


def informativos_eliminatoria():
    nome = "C"
    pts = "W"
    inicio = 3
    tabelas = ["leliminatoria_ccap", "leliminatoria_scap"]
    for tab in tabelas:
        planilha = acessar_arquivo(tab)
        times = bd_dict_list(tabela=tab, coluna="Pts")
        contador = 0
        for t in times:
            num = inicio + contador
            planilha[f'{nome}{num}'] = t['Nome']
            planilha[f'{pts}{num}'] = t['Pts']
            contador += 2


