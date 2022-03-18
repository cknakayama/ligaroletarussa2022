from bd import *
from api import *


con, cursor = acesso_mysql()
cursor.execute("SELECT Rodada1 FROM mmliga")
print(cursor.fetchall()[0][0])

x = bd_dict_list("mmliga")
#x = bd_dict_list("mmliga")
print(x)
