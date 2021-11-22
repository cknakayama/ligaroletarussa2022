import cartola_funcionalidades
import mysql.connector

con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="roleta_russa_2022"
    )
cursor = con.cursor()
cursor.execute("SELECT * FROM autenticacao;")
x = cursor.fetchall()
y = x[0][0]
print(type(y))