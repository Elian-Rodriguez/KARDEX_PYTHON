import Conexion
import re
def listar_Marca():
    curs =Conexion.cursor()
    curs.execute("SELECT * FROM Kardex_monitor.Marca;")
    dat = curs.fetchall()
    return dat
def listar_Estado():
    curs =Conexion.cursor()
    curs.execute("SELECT * FROM Kardex_monitor.Estado;")
    dat = curs.fetchall()
    return dat

def listar_Tipo_dispositivo():
    curs =Conexion.cursor()
    curs.execute("SELECT * FROM Kardex_monitor.Tipo_dispositivo;")
    dat = curs.fetchall()
    mysql=Conexion.conexionmysql()
    mysql.commit()
    return dat


def create_marca(nommarca):
    if nommarca and nommarca.strip():
        curs =Conexion.cursor()
        curs.execute("SELECT max(idMarca) FROM Kardex_monitor.Marca;")
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
        sentencia = "INSERT INTO `Kardex_monitor`.`Marca` (`idMarca`, `Nombre_Marca`)  VALUES ("+id+", '"+nommarca+"');"
        curs.execute(sentencia)
        mysql=Conexion.conexionmysql()
        mysql.commit()
        return "CREACION DE MARCA CON EXITO"
        
    else :
        return "FALTAN DATOS PARA LA CREACION DEL MARCA"


    
def create_Estado(nombre_estado):
    if nombre_estado and nombre_estado.strip():
        curs =Conexion.cursor()
        curs.execute("SELECT max(idEstado) FROM Kardex_monitor.Estado;")
        dat = curs.fetchall()
        valor = (dat[0])
        valor = str(valor) 
        string = valor
        string = re.sub("\(|\'|\?","",string)
        string = re.sub("\,|\'|\?","",string)
        string = re.sub("\)|\'|\?","",string)
        valor = int(string) +1
        id= str(valor)
        sentencia = "INSERT INTO `Kardex_monitor`.`Estado` (`idEstado`, `Nombre_estado`) VALUES ("+id+", '"+nombre_estado+"');"
        curs.execute(sentencia)
        mysql=Conexion.conexionmysql()
        mysql.commit()
        return "CREACION DE ESTADO CON EXITO"
        
    else :
        return "FALTAN DATOS PARA LA CREACION DEL ESTADO"


def create_Tp_dispositivo(Tp_dispositivo):
    if Tp_dispositivo and Tp_dispositivo.strip():
        curs =Conexion.cursor()
        curs.execute("SELECT max(idTipo_dispositivo) FROM Kardex_monitor.Tipo_dispositivo;")
        dat = curs.fetchall()
        valor = (dat[0])
        valor = str(valor) 
        string = valor
        string = re.sub("\(|\'|\?","",string)
        string = re.sub("\,|\'|\?","",string)
        string = re.sub("\)|\'|\?","",string)
        valor = int(string) +1
        id= str(valor)
        sentencia = "INSERT INTO `Kardex_monitor`.`Tipo_dispositivo` (`idTipo_dispositivo`, `Nombre_tip_dispo`) VALUES ("+id+", '"+Tp_dispositivo+"');"
        curs.execute(sentencia)
        mysql=Conexion.conexionmysql()
        mysql.commit()
        return "CREACION DE TIPO DE DISPOSITIVO CON EXITO"
        
    else :
        return "FALTAN DATOS PARA LA CREACION DEL TIPO DE DISPOSITIVO"


  
    
    


#print (create_Tp_dispositivo("IMPRESORA"))



    