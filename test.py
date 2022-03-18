from bd import *
from api import *


#con, cursor = acesso_mysql()
#cursor.execute("SELECT ID FROM mmliga")
#print(cursor.fetchall())

x = pesquisar_time()
salvar_time_bd(x, "mmliga")
atualizar_nomes_times("mmliga")
print(x)
