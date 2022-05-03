from bd import *
from api import *
from roleta_russa import *
from informativos import *


con, cursor = acesso_mysql()
cursor.execute("SELECT ID, Nome, Rodada4 FROM lprincipal_scap ORDER BY Rodada4 DESC;")
lista = cursor.fetchall()
lista_times = []
for time in lista:
    t = {"ID": time[0], "Nome": time[1], "Pontos": time[2]}
    lista_times.append(t)
listar_itens(lista_times)
