import os
import subprocess
from subprocess import check_output

print ("Resultados de mysql.connector:")
import pymysql

miConexion = pymysql.connect( host='10.26.1.161', user= 'bart',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()
#decendente
cur.execute( """  SELECT * FROM TIENDAS.Tienda WHERE Abierta =1; """ )

datos = cur.fetchall()
"
nombre = "Ejecucion_Validador.sh"

COMANDO =""" #! /bin/bash """
COMANDO=COMANDO+"""\n date"""


Ejecucion = """  "cat /home/NCR/webfront/conf/webfrontenv.properties;cat /etc/hosts | grep REG ;" """

for shop in datos:
    IP=shop[3]
    COD_POS= shop[0]
    Clave="/home/kardex/SERVER/NCR"
    COMANDO =COMANDO + "\nsudo sshpass  -f "+Clave+" ssh -o StrictHostKeyChecking=no root@"+IP+Ejecucion+"""> /home/kardex/SERVER/VALIDAR_HOST/"""+str(COD_POS)+""".txt ; """


COMANDO=COMANDO+"""\ndate ;"""

from os import system



archivo = open(nombre,'w')
archivo.write(COMANDO)
archivo.close()



#print(COMANDO)
miConexion.close()



