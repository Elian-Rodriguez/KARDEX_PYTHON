import os
import subprocess
from subprocess import check_output

import pymysql

miConexion = pymysql.connect( host='10.26.1.161', user= 'lisa',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()
cur.execute( """SELECT * FROM Kardex_monitor.Conf_pos order by Tiendas_Cod_Ncr DESC;""" )

datos = cur.fetchall()


for shop in datos:
    IP=shop[1]
    COD_POS= shop[0]
    Clave=shop[2]
    file_name=COD_POS+".txt"
    archivo = open(file_name,'r')
    marca_impresora = archivo.read()
    archivo.close()
    ACT=f"UPDATE `Kardex_monitor`.`Conf_pos` SET `Impresora` = '"+marca_impresora+"' WHERE (`idConf_pos` = '"+COD_POS+"');"
    print ("consulta realizada con exito "+COD_POS +"\n")
    cur.execute(ACT)
    miConexion.commit()
    
    #cur.commit()

    

#print(COMANDO)
miConexion.close()
