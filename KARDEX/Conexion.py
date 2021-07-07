import mysql.connector
import pymysql


miConexion = pymysql.connect( host='10.26.1.161', user= 'kardex',port=3306, passwd='Linux-1234', db='Kardex_monitor' )



def conexionmysql():
    try:
        return miConexion
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        Error = "Ocurrió un error al conectar: " + e
        return Error
    
def filalizarconexionmysql(myconexion):
    myconexion.close()
    
    
def cursor():
    
    cur = miConexion.cursor()
    return cur
