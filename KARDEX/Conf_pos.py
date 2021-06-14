import Conexion
def listar_pos():
    curs =Conexion.cursor()
    curs.execute("SELECT * FROM Kardex_monitor.Conf_pos order by Tiendas_Cod_Ncr asc;")
    dat = curs.fetchall()
    return dat