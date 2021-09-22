import Conexion
mysql = Conexion.cmysql()
def listar_location():
    curs =Conexion.cmysql().cursor()
    curs.execute("SELECT * FROM Kardex_monitor.Tiendas ORDER BY Codigo_sap ASC;")
    dat = curs.fetchall()
    return dat


