# INSERT INTO `Kardex_monitor`.`Activo` (`Serial`, `Estado_idEstado`, `ACT_Ingreso_id_ACt_ingreso`, `Modelo_idModelo`, `Ubicacionact_Cod_Ncr`) VALUES ('1', '2', '1', '2', '2');

import Conexion
import re
from datetime import date
from datetime import datetime
mysql = Conexion.cmysql()


def listar_activo():
    curs =Conexion.cmysql().cursor()
    curs.execute("call Kardex_monitor.Listar_activos();")
    dat = curs.fetchall()
    return dat
def crear_Activo(Serial , Estado_idEstado , ACT_Ingreso_id_ACt_ingreso , Modelo_idModelo , Ubicacionact_Cod_Ncr):
    if Serial and Serial.strip() or Estado_idEstado.strip() or ACT_Ingreso_id_ACt_ingreso.strip() or Modelo_idModelo.strip() or Ubicacionact_Cod_Ncr.strip() :
        curs =Conexion.cmysql().cursor()
        fecha = date.today()

        print(fecha)
        fecha= str(fecha)
        Serial = str(Serial)
        Estado_idEstado = str(Estado_idEstado)
        ACT_Ingreso_id_ACt_ingreso = str(ACT_Ingreso_id_ACt_ingreso)
        Modelo_idModelo = str(Modelo_idModelo)
        Ubicacionact_Cod_Ncr = str(Ubicacionact_Cod_Ncr)
        sentencia = "INSERT INTO `Kardex_monitor`.`Activo` (`Serial`, `Estado_idEstado`, `ACT_Ingreso_id_ACt_ingreso`, `Modelo_idModelo`, `Ubicacionact_Cod_Ncr`, `ultima_modificacion`) VALUES   ('"+Serial+"', '"+Estado_idEstado+"', '"+ACT_Ingreso_id_ACt_ingreso+"', '"+Modelo_idModelo+"', '"+Ubicacionact_Cod_Ncr+"', '"+fecha+"');"
        curs.execute(sentencia)
        mysql.commit()
        return "CREACION DE MARCA CON EXITO"
    else :
        return "FALTAN DATOS PARA LA CREACION DEL MARCA"


def buscar_serial(seria_bus):
    if seria_bus and seria_bus.strip():
        sentencia = """call Kardex_monitor.Buscar_seriales('"""+seria_bus+"""');"""
        curs =Conexion.cmysql().cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
        return dat
    else:
        dat =""
        return dat


def buscar_unico_serial(seria_bus):
    if seria_bus and seria_bus.strip():
        sentencia = """call Kardex_monitor.filtro_serial('"""+seria_bus+"""');"""
        curs =Conexion.cmysql().cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
        return dat
    else:
        dat =""
        return dat


def filtrar_ubicacion(ubicacion):
    if ubicacion and ubicacion.strip():
        sentencia = """call Kardex_monitor.Filtrar_cod_sap_tienda('"""+ubicacion+"""');"""
        curs =Conexion.cmysql().cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
        return dat
    else:
        dat =""
        return dat

def acutalizar_estado_activo(serial,id_estado):
    if serial.strip() or id_estado.strip():
        curs =Conexion.cmysql().cursor()
        #UPDATE `Kardex_monitor`.`Activo` SET `Estado_idEstado` = '2' WHERE (`Serial` = 'pb2');
        sentencia = """UPDATE `Kardex_monitor`.`Activo` SET `Estado_idEstado` = '"""+id_estado+"""' WHERE (`Serial` = '"""+serial+"""'); """
        print (sentencia)
        curs.execute(sentencia)
        mysql.commit()
        return "ACTUALIZACION DE ACTIVO CON EXITO"


#UPDATE `Kardex_monitor`.`Activo` SET `Ubicacionact_Cod_Ncr` = '2' WHERE (`Serial` = 'pb2');


def acutalizar_ubicacion_activo(serial,codncr):
    if serial.strip() or codncr.strip():
        curs =Conexion.cmysql().cursor()
        #UPDATE `Kardex_monitor`.`Activo` SET `Estado_idEstado` = '2' WHERE (`Serial` = 'pb2');
        sentencia = """UPDATE `Kardex_monitor`.`Activo` SET `Ubicacionact_Cod_Ncr` = '"""+codncr+"""' WHERE (`Serial` = '"""+serial+"""'); """
        print (sentencia)
        curs.execute(sentencia)
        mysql.commit()
        return "ACTUALIZACION DE ACTIVO CON EXITO"

def filtrar_tienda(sap):
    if sap and sap.strip():
        sentencia = """call Kardex_monitor.Exportar_Act_SAP_EXCEL('"""+sap+"""');"""
        curs =Conexion.cmysql().cursor()
        curs.execute(sentencia)
        dat = curs.fetchall()
       
        return dat
    else:
        dat ="NO HAY DATA"
        return dat
    
def listar_ubucacion_local():
    sentencia = """SELECT * FROM Kardex_monitor.ubicacion_local;"""
    curs =Conexion.cmysql().cursor()
    curs.execute(sentencia)
    dat = curs.fetchall()
    return dat

def actualizar_ubicacion_tienda(serial,ubicacion_tienda):
    Serial=str(serial)
    localizacion=str(ubicacion_tienda)
    sentencia="""UPDATE `Kardex_monitor`.`Activo` SET `local_ubicacion` = '"""+str(localizacion)+"""' WHERE (`Serial` = '"""+str(Serial)+"""');"""
    
    curs =Conexion.cmysql().cursor()
    curs.execute(sentencia)
    mysql.commit()

