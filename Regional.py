import app as app,mysql
def Crear_regional(IdRegional, CODIGOSAP,  NombreRegional):
        cur = mysql.connection.cursor()
        #INSERT INTO `INVENTARIO_BOGOTA`.`Regional` (`idRegional`, `Codigo_sap_Regional`, `Codigo_sap_Regional`) VALUES ('2', '2', '2');
        cur.execute('INSERT INTO INVENTARIO_BOGOTA.Regional (idRegional, Codigo_sap_Regional, Nombre_Regional) VALUES(%s, %s, %s ); ',
            (IdRegional, CODIGOSAP,  NombreRegional))
        mysql.connection.commit()
        
def Listar_Regional():
    cur = mysql.connection.cursor()
    sentens = ('SELECT * FROM INVENTARIO_BOGOTA.Regional;')
    cur.execute(sentens)
    datas = cur.fetchall()
    return datas