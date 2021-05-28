from app import app,mysql


def Crear_regional(IdRegional, CODIGOSAP,  NombreRegional):
        cur = mysql.connection.cursor()
        #INSERT INTO `INVENTARIO_BOGOTA`.`Regional` (`idRegional`, `Codigo_sap_Regional`, `Codigo_sap_Regional`) VALUES ('2', '2', '2');
        cur.execute('INSERT INTO Kardex_monitor.Regional (Cod_Regional, Codigo_Sap, Nombre_Regional) VALUES(%s, %s, %s ); ',
            (IdRegional, CODIGOSAP,  NombreRegional))
        mysql.connection.commit()
        
def Listar_Regional():
    cur = mysql.connection.cursor()
    print("cursor ejecutado")
    sentens = ('SELECT * FROM Regional;')
    print("consulta realizada")
    cur.execute(sentens)
    datas = cur.fetchall()
    return datas


dat= Listar_Regional()
print(dat)