import Conexion
mysql = Conexion.cmysql()
def listar_pos():
    curs =Conexion.cmysql().cursor()
    curs.execute("SELECT * FROM Kardex_monitor.Conf_pos order by Tiendas_Cod_Ncr asc;")
    dat = curs.fetchall()
    return dat