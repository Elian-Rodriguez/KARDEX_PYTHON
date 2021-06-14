# INSERT INTO `Kardex_monitor`.`Activo` (`Serial`, `Estado_idEstado`, `ACT_Ingreso_id_ACt_ingreso`, `Modelo_idModelo`, `Ubicacionact_Cod_Ncr`) VALUES ('1', '2', '1', '2', '2');

import Conexion 
import re
from datetime import date
from datetime import datetime
def listar_activo():
    curs =Conexion.cursor()
    curs.execute("call Kardex_monitor.Listar_activos();")
    dat = curs.fetchall()
    return dat
def crear_Activo(Serial , Estado_idEstado , ACT_Ingreso_id_ACt_ingreso , Modelo_idModelo , Ubicacionact_Cod_Ncr):
    if Serial and Serial.strip() or Estado_idEstado.strip() or ACT_Ingreso_id_ACt_ingreso.strip() or Modelo_idModelo.strip() or Ubicacionact_Cod_Ncr.strip() :
        curs =Conexion.cursor()
        
        fecha = date.today()
        
        print(fecha)
        fecha= str(fecha)       
        Serial = str(Serial) 
        Estado_idEstado = str(Estado_idEstado)
        ACT_Ingreso_id_ACt_ingreso = str(ACT_Ingreso_id_ACt_ingreso)
        Modelo_idModelo = str(Modelo_idModelo)
        Ubicacionact_Cod_Ncr = str(Ubicacionact_Cod_Ncr)  
        
        sentencia = "INSERT INTO `Kardex_monitor`.`Activo` (`Serial`, `Estado_idEstado`, `ACT_Ingreso_id_ACt_ingreso`, `Modelo_idModelo`, `Ubicacionact_Cod_Ncr`, `ultima_modificacion`) VALUES   ('"+Serial+"', '"+Estado_idEstado+"', '"+ACT_Ingreso_id_ACt_ingreso+"', '"+Modelo_idModelo+"', '"+Ubicacionact_Cod_Ncr+"', '"+fecha+"');"
        print (sentencia)
        curs.execute(sentencia)
        mysql=Conexion.conexionmysql()
        mysql.commit()
        return "CREACION DE MARCA CON EXITO"
                                                                          
    else :
        return "FALTAN DATOS PARA LA CREACION DEL MARCA"
    
def buscar_serial(seria_bus):
    if seria_bus and seria_bus.strip():
        sentencia = """call Kardex_monitor.Buscar_seriales('"""+seria_bus+"""');"""
        curs =Conexion.cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
        return dat
    else:
        dat =""
        return dat
    
    
    
def buscar_unico_serial(seria_bus):
    if seria_bus and seria_bus.strip():
        sentencia = """call Kardex_monitor.filtro_serial('"""+seria_bus+"""');"""
        curs =Conexion.cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
        return dat
    else:
        dat =""
        return dat    
    
def filtrar_ubicacion(ubicacion):
    if ubicacion and ubicacion.strip():
        sentencia = """call Kardex_monitor.Filtrar_cod_sap_tienda('"""+ubicacion+"""');"""
        curs =Conexion.cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
        return dat
    else:
        dat =""
        return dat
    
def acutalizar_estado_activo(serial,id_estado):
    if serial.strip() or id_estado.strip():
        curs =Conexion.cursor()
        #UPDATE `Kardex_monitor`.`Activo` SET `Estado_idEstado` = '2' WHERE (`Serial` = 'pb2');
        sentencia = """UPDATE `Kardex_monitor`.`Activo` SET `Estado_idEstado` = '"""+id_estado+"""' WHERE (`Serial` = '"""+serial+"""'); """
        print (sentencia)
        curs.execute(sentencia)
        mysql=Conexion.conexionmysql()
        mysql.commit()
        return "ACTUALIZACION DE ACTIVO CON EXITO"


#UPDATE `Kardex_monitor`.`Activo` SET `Ubicacionact_Cod_Ncr` = '2' WHERE (`Serial` = 'pb2');


def acutalizar_ubicacion_activo(serial,codncr):
    if serial.strip() or codncr.strip():
        curs =Conexion.cursor()
        #UPDATE `Kardex_monitor`.`Activo` SET `Estado_idEstado` = '2' WHERE (`Serial` = 'pb2');
        sentencia = """UPDATE `Kardex_monitor`.`Activo` SET `Ubicacionact_Cod_Ncr` = '"""+codncr+"""' WHERE (`Serial` = '"""+serial+"""'); """
        print (sentencia)
        curs.execute(sentencia)
        mysql=Conexion.conexionmysql()
        mysql.commit()
        return "ACTUALIZACION DE ACTIVO CON EXITO"
    
def filtrar_tienda(sap):
    if sap and sap.strip():
        sentencia = """call Kardex_monitor.Exportar_Act_SAP_EXCEL('"""+sap+"""');"""
        curs =Conexion.cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
        return dat
    else:
        dat =""
        return dat