"""
Funções para exibir e interagir com algo no console.
"""
from os import system


def exibir_cabecalho(texto: str = ''):
    system('cls') or None
    print('-' * 50)
    print(f"|{texto.upper():^48}|")
    print('-' * 50)


def listar_itens(lista: list):
    """
    Método que exibe na tela uma lista tabelada das opções.

    Recebe:     lista - uma lista de dicionários contendo as opções.
                As chaves serão os cabeçalhos da tabela.
    """
    chaves = [key for key in lista[0].keys()]
    maiores = []
    for chave in chaves:
        valor_maior = 0
        for item in lista:
            if len(str(item[chave])) > valor_maior:
                valor_maior = len(str(item[chave]))
            else:
                pass
        maiores.append(valor_maior)
    print(f" {'No':_^4} ", end="")
    for c in range(0, len(chaves)):
        print(f" {chaves[c].upper():_^{maiores[c] + 2}} ", end="")
    print()
    numero = 1
    for dic in lista:
        print(f" {numero:^4} ", end="")
        for c in range(0, len(chaves)):
            print(f" {dic[chaves[c]]:<{maiores[c] + 2}} ", end="")
        print()
        numero += 1
    print(f" {'0':^4}  Nenhuma das alternativas")


def int_input(texto: str = ''):
    """
    Método para garantir que a entada será um inteiro.
    """
    while True:
        try:
            entrada = int(input(texto))
        except ValueError:
            print('Digite um valor válido.')
        else:
            break
    return entrada


def escolher_entre_opcoes(dicionario: list):
    """"
    Método que devolve a opção escolhida.

    Recebe:     dicionario - lista de dicionários com as opções.

    Retorna:    dicionário com a opção escolhida ou um dicionário vazio.
    """
    while True:
        escolha = int_input(
            f'Escolha uma das opções entre 1 e {len(dicionario)} ou 0 e digite aqui sua escolha: ')
        if escolha == 0:
            return {}
        elif 0 < escolha <= len(dicionario):
            return dicionario[escolha - 1]
        else:
            print('Opção inválida.')
