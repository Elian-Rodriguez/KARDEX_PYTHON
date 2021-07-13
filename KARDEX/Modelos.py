#INSERT INTO `Kardex_monitor`.`Modelo` (`idModelo`, `Nombre_modelo`, `Marca_idMarca`, `Tipo_dispositivo_idTipo_dispositivo`) VALUES ('1', 'LIDE 300', '5', '9');

import Conexion
import re
def listar_modelo():
    curs =Conexion.cursor()
    curs.execute("call Kardex_monitor.Listar_Modelo_marca_tp_dispo();")
    dat = curs.fetchall()
    return dat
def crear_modelo(modelo,marca,Tipo_disp):
    if modelo and modelo.strip() or marca.strip() or Tipo_disp.strip():
        curs =Conexion.cursor()
        curs.execute("SELECT max(idModelo) FROM Kardex_monitor.Modelo;")
        dat = curs.fetchall()
        valor = (dat[0])
        valor = str(valor)
        string = valor
        string = re.sub("\(|\'|\?","",string)
        string = re.sub("\,|\'|\?","",string)
        string = re.sub("\)|\'|\?","",string)
        valor = int(string) +1
        id= str(valor)
        #INSERT INTO `Kardex_monitor`.`Marca` (`idMarca`, `Nombre_Marca`) VALUES ('2', 'CISCO');
        sentencia = "INSERT INTO `Kardex_monitor`.`Modelo` (`idModelo`, `Nombre_modelo`, `Marca_idMarca`, `Tipo_dispositivo_idTipo_dispositivo`) VALUES  ('"+id+"', '"+modelo+"', '"+marca+"', '"+Tipo_disp+"');"
        curs.execute(sentencia)
        mysql=Conexion.conexionmysql()
        mysql.commit()
        return "CREACION DE MARCA CON EXITO"
    else :
        return "FALTAN DATOS PARA LA CREACION DEL MARCA"
