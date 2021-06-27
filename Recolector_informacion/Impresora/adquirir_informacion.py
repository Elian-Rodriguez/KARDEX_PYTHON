import os
import subprocess
from subprocess import check_output

print ("Resultados de mysql.connector:")
import pymysql
#acendente
miConexion = pymysql.connect( host='10.28.0.154', user= 'bart',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()
POS = "REG001"
cur.execute( """  SELECT * FROM Kardex_monitor.Conf_pos where  idConf_pos like "%"""+POS+ """%" ORDER BY Tiendas_Cod_Ncr ASC ;  """ )

datos = cur.fetchall()
#--nombre =input("INTRODUSCA EL NOMBRE DEL ARCHIVO : ")+".sh"
nombre = "Ejecucion_Validador_espacio_1.sh"
#print("El ARCHIVO SE VA ALMACENAR CON EL NOMBRE :"+nombre)
COMANDO =""" #! /bin/bash """
COMANDO=COMANDO+"""\ndate ;""" 
for shop in datos:
    IP=shop[1]
    COD_POS= shop[0]
    Clave=shop[2]
    Ejecucion = """  "df -hl /home " """
    COMANDO =COMANDO + "\nsudo sshpass  -f "+Clave+" ssh -o StrictHostKeyChecking=no root@"+IP+Ejecucion+"""; """
COMANDO=COMANDO+"""\ndate ;""" 
print (COMANDO)
from os import system



archivo = open(nombre,'w')
archivo.write(COMANDO)
archivo.close()
#decendente
cur.execute( """  SELECT * FROM Kardex_monitor.Conf_pos where  idConf_pos like "%"""+POS+ """%" ORDER BY Tiendas_Cod_Ncr DESC ;  """ )

datos = cur.fetchall()
#--nombre =input("INTRODUSCA EL NOMBRE DEL ARCHIVO : ")+".sh"
nombre = "Ejecucion_Validador_espacio_2.sh"
#print("El ARCHIVO SE VA ALMACENAR CON EL NOMBRE :"+nombre)
COMANDO =""" #! /bin/bash """
COMANDO=COMANDO+"""\ndate ;""" 
for shop in datos:
    IP=shop[1]
    COD_POS= shop[0]
    Clave=shop[2]
    COMANDO =COMANDO + "\nsudo sshpass  -f "+Clave+" ssh -o StrictHostKeyChecking=no root@"+IP+Ejecucion+"""; """

COMANDO=COMANDO+"""\ndate ;""" 

from os import system



archivo = open(nombre,'w')
archivo.write(COMANDO)
archivo.close()



#print(COMANDO)
miConexion.close()



