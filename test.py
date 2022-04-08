from bd import *
from api import *
from roleta_russa import *


slugs = ["roleta-ru-a", "roleta-russa-a-liga"]

times = times_liga(slugs[0])
for time in times:
    CadastrarTime(time, "lprincipal_ccap")

