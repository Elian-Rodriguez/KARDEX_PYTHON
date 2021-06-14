import Conexion
class Comarca:
    def listar_comarca():
        curs =Conexion.cursor()
        curs.execute("SELECT * FROM Kardex_monitor.Regional;")
        dat = curs.fetchall()
        return dat

    def crear_comarca(Id, SAP, Regional):
        curs =Conexion.cursor()
        curs.execute('INSERT INTO `Kardex_monitor`.`Regional` (`Cod_Regional`, `Codigo_Sap`, `Nombre_Regional`) VALUES(%s, %s, %s); ',
                            (Id, SAP, Regional))
        mysql=Conexion.conexionmysql()
        mysql.commit()
    def eliminar_comarca(id):
        curs =Conexion.cursor()
        mysql=Conexion.conexionmysql()
        curs.execute(
            'DELETE FROM `Kardex_monitor`.`Regional` WHERE (`Cod_Regional` = {0});'.format(id))
        mysql.commit()
        


