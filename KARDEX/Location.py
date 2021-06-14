import Conexion
def listar_location():
    curs =Conexion.cursor()
    curs.execute("SELECT * FROM Kardex_monitor.Tiendas;")
    dat = curs.fetchall()
    return dat


