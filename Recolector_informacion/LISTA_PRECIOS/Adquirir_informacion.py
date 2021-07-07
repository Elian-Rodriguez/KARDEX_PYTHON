import os
import subprocess
from subprocess import check_output

print ("Resultados de mysql.connector:")
import pymysql
#acendente
miConexion = pymysql.connect( host='10.28.0.154', user= 'bart',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()
POS = "REG001"
cur.execute( """ SELECT Cod_Ncr,Ip_Server FROM Kardex_monitor.Tiendas where abierta =1 order by Cod_Ncr asc;  """ )

datos = cur.fetchall()
#--nombre =input("INTRODUSCA EL NOMBRE DEL ARCHIVO : ")+".sh"
nombre = "Ejecucion_Validador_espacio_1.sh"
#print("El ARCHIVO SE VA ALMACENAR CON EL NOMBRE :"+nombre)
COMANDO =""" #! /bin/bash """
COMANDO=COMANDO+"""\ndate ;""" 
for shop in datos:
    IP=shop[1]
    COD_POS= shop[0]
    Clave= "NCR"
    Ejecucion = """   sh /home/NCRServices/InterfaceService/ConsultaCarguePrecios.sh  """
    COMANDO =COMANDO + "\nsudo sshpass  -f "+Clave+" ssh -o StrictHostKeyChecking=no root@"+IP+Ejecucion+""" >"""+COD_POS+""".txt; """
COMANDO=COMANDO+"""\ndate ;""" 
print (COMANDO)
from os import system



archivo = open(nombre,'w')
archivo.write(COMANDO)
archivo.close()