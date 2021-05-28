import app as app,mysql
mysqls = mysql

def Crear_regional(IdRegional, CODIGOSAP,  NombreRegional):
        cur = mysqls.connection.cursor()
      
      
def Listar_Regional():
    cur = mysqls.connection.cursor()
    print("cursor ejecutado")
    cur.execute('SELECT * FROM Kardex_monitor.Regional;')
    datas = cur.fetchall()
    return datas

#INSERT INTO `Kardex_monitor`.`Regional` (`Cod_Regional`, `Codigo_Sap`, `Nombre_Regional`) VALUES ('6030', '6A06', 'BOGOTA');

dat= Listar_Regional()
print(dat)