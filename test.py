from bd import nomes_colunas, bd_dict
from api import times_liga


x = times_liga("roleta-ru-a")
y = x[0].keys()
for i in y:
    print(i)

