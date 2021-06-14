import mysql.connector
import pymysql



miConexion = pymysql.connect( host='10.26.1.161', user= 'lisa',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()

def conexionmysql():
    return miConexion
def cursor():
    return cur
