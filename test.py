from bd import *
from api import *


con, cursor = acesso_mysql()
cursor.execute("SELECT Rodada1 FROM mmliga")
print(cursor.fetchall())

x = bd_dict_list("mmliga")
#x = bd_dict_list("mmliga")
print(x)

x = None
y = 100
if y > x:
    print("SIM")
