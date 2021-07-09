
from re import A
import re
from flask import Flask, render_template, request, redirect, url_for, flash,Response
from flask_mysqldb import MySQL
import io
import xlwt
from Comarcas import Comarca
import Location ,Conf_pos,Generalidad,Modelos,Activo,Acta_ingreso
from datetime import date
from datetime import datetime
from PIL import Image
#librerias nuevas
from  flask_mail import Mail,Message




app = Flask(__name__)

app.config['MYSQL_HOST'] = '10.26.1.161'
app.config['MYSQL_USER'] = 'kardex'
app.config['MYSQL_PASSWORD'] = 'Linux-1234'
app.config['MYSQL_DB'] = 'Kardex_monitor'
mysql = MySQL(app)

#Configurar sesion
app.secret_key = "mysecretkey"


#Configuracion de servidor de correo 900276962KOBA 900276962KOBA
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME'] = 'kardexregbogota@gmail.com'
app.config['MAIL_PASSWORD'] ='900276962KOBA'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#creacion de objeto mail server
mail = Mail(app)

#Definicion de rutas y configuracion
@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/LISTAR_ENVIAR')
def LISTAR_ENVIAR() :
    data=Location.listar_location()
    return render_template('Listar_Enviar.html',ubicaciones=data)

@app.route('/Envira_acta_entrega', methods=['POST'])
def Envira_acta_entrega():
    if request.method == 'POST':
        correojdz ='elianeduardor451@gmail.com'
        tienda = "6A060999 PRUEBAS "
        Asunto = "Acta de Entrega de Equipos de la tienda "+tienda
        msg = Message (Asunto , sender ='kardexregbogota@gmail.com',recipients =['jose.lara@koba-group.com','freddy.barreto@koba-group.com','jorge.leon@koba-group.com',correojdz])
        msg.body = """BUEN DIA
        ADJUNTO  LISTADO DE DISPOSITIVOS ASIGNADOS A LA TIENDA  """+tienda+""" DICHO CAMBIO REALIZADO EL DIA """ +str(datetime.today())+"""
        
        """
        mail.send(msg)
    return redirect(url_for('LISTAR_ENVIAR'))

@app.route('/Regional')
def Regional():
    data = Comarca.listar_comarca()
    return render_template('Regional.html',regionales =  data)

@app.route('/create_regional', methods=['POST'])
def create_regional():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        IdRegional=request.form['Id_Regional']
        CODIGOSAP=request.form['CODIGO_SAP']
        NombreRegional=request.form['Nombre_Regional']
        Comarca.crear_comarca(IdRegional,CODIGOSAP,NombreRegional)
        flash('COMARCA INGRESADA CORRECTAMENTE')
    return redirect(url_for('Regional'))





@app.route('/Ubicacion')
def Ubicacion():
    data=Location.listar_location()
    data2= Comarca.listar_comarca()
    return render_template('Ubicacion.html',ubicaciones=data ,comarcas=data2)


@app.route('/create_ubicacion', methods=['POST'])
def create_ubicacion():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        CODNCR = request.form['COD_NCR']
        Nombreubicacion = request.form['Nombre_ubicacion']
        CODIGOSAP = request.form['CODIGO_SAP']
        IPSERVER = request.form['IP_SERVER']
        IPPC = request.form['IP_PC']
        CAMARA = request.form['IP_ CAMARAS']
        ABIERT = request.form['ABIERTA']
        ESTAD = request.form['ESTADO']
        IdRegional=request.form['Regional']
   
        cur.execute("""INSERT INTO `Kardex_monitor`.`Tiendas` (`Cod_Ncr`, `Nombre_Tienda`, `Codigo_sap`, `Ip_Server`, `Ip_Pc`, `Ip_Camaras`, `Abierta`, `Estado`, `Regional_Cod_Regional`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s); """,
                        (CODNCR, Nombreubicacion, CODIGOSAP,IPSERVER,IPPC,CAMARA,ABIERT,ESTAD,IdRegional))
        mysql.connection.commit()
        flash('COMARCA INGRESADA CORRECTAMENTE')
    return redirect(url_for('Ubicacion'))
   



@app.route("/Marca")
def Marca():
    data= Generalidad.listar_Marca()
    data2=Generalidad.listar_Estado()
    data3=Generalidad.listar_Tipo_dispositivo()
    return render_template('Marca.html',Marcas=data,ESTADOS=data2,TP_DISPOSITIVOS=data3)
    
@app.route('/create_marca', methods=['POST'])
def create_marca():
    if request.method == 'POST':
        NOMBRE_MARCA=request.form['NOMBRE_MARCA']
        Generalidad.create_marca(NOMBRE_MARCA)
    return redirect(url_for('Marca'))


@app.route('/create_estado', methods=['POST'])
def create_estado():
    if request.method == 'POST':
        NOMBRE_ESTADO=request.form['NOMBRE_ESTADO']
        flash(Generalidad.create_Estado(NOMBRE_ESTADO))
    return redirect(url_for('Marca'))
@app.route('/create_tp_dispositivo', methods=['POST'])
def create_tp_dispositivo():
    if request.method == 'POST':
        NOMBRE_TP_DISPOSITIVO=request.form['NOMBRE_TP_DISPOSITIVO']
        flash(Generalidad.create_Tp_dispositivo(NOMBRE_TP_DISPOSITIVO))
    return redirect(url_for('/Marca'))

@app.route("/POS_TIENDA")
def POS_TIENDA():
    data=Location.listar_location()
    dats2=Conf_pos.listar_pos()
    return render_template('POS_TIENDA.html',comarcas=data,modulos=dats2)

@app.route("/Modelo")
def Modelo():
    data = Modelos.listar_modelo()
    data2 = Generalidad.listar_Marca()
    data3 = Generalidad.listar_Tipo_dispositivo()
    return render_template('Modelo.html',modelos=data,marcas = data2 , tp_dispo = data3 )


@app.route("/create_modelo" , methods=['POST'])
def create_modelo():
    if request.method == 'POST':
        Id_modelo = request.form['Id_modelo']
        ID_marca =  request.form['Marca']
        ID_tp_dispo = request.form['tipo_dispo']
        modelos = request.form['Nombre_Modelo']
        Modelos.crear_modelo(modelos,ID_marca,ID_tp_dispo)
    return redirect(url_for('Modelo'))
        
@app.route("/crear_dispositivo")
def crear_dispositivo():
    data = Activo.listar_activo()
    data2 =Modelos.listar_modelo()
    data3 = Generalidad.listar_Estado()
    data4 = Location.listar_location()
    data5 = Acta_ingreso.listar_actas()
    return render_template('Crear_dispositivo.html', dispositivos = data,
                           modelos = data2, estados = data3,ubicaciones= data4, actingresos = data5)


@app.route("/acta_ingreso")
def acta_ingreso():
    data = Acta_ingreso.listar_actas()
    return render_template('Acta_ingreso.html',acts = data)

@app.route("/create_ingreso", methods=['POST'])
def create_ingreso():
    if request.method == 'POST':
        fecha= request.form['fecha_ingreso']
        print(fecha)
    return redirect(url_for('acta_ingreso'))


@app.route("/create_activo", methods=['POST'])
def create_activo():
    if request.method == 'POST':
        Serial = request.form['Serial']
        estado = request.form['estado']
        act_ingreso = request.form['act_ingreso']
        Modelo = request.form['Modelo']
        ubicacion = request.form['ubicacion']
        Activo.crear_Activo(Serial,estado,act_ingreso,Modelo,ubicacion)
        return crear_dispositivo()


@app.route("/buscar_act", methods=['POST'])
def buscar_act():
    if request.method == 'POST':
        serial_buscar= request.form['Serial_buscar']
        data = Activo.buscar_serial(serial_buscar)
        return render_template('Listar_editar.html', resultados =data)
    else :
        return redirect(url_for('crear_dispositivo'))


@app.route("/buscar_act_ubicacion", methods=['POST'])
def buscar_act_ubicacion():
    if request.method == 'POST':
        serial_buscar= request.form['SAP']
        data = Activo.filtrar_ubicacion(serial_buscar)
        return render_template('Listar_editar.html', resultados =data)
    else :
        return redirect(url_for('crear_dispositivo'))


@app.route('/edit_device/<string:Serial>')
def edit_device(Serial):
    data = Activo.buscar_unico_serial(Serial)
    data3 = Generalidad.listar_Estado()
    data4 = Location.listar_location()
    return render_template('Activo_editar.html', shop=data[0], estados = data3,ubicaciones= data4)

    
    
    
@app.route('/update_device/<string:Serial>', methods=['POST'])
def update_device(Serial):
    if request.method == 'POST':
        serialact = request.form['SERIAL']
        id_estadonuevo= request.form['NUEVOESTADO']
        id_ubicacionnueva= request.form['NUEVAUBICACION']
        if request.form.get('actualizar_estado_ubicacion') == 'actualizar_estado_ubicacion':
           Activo.acutalizar_estado_activo(serialact,id_estadonuevo)
           Activo.acutalizar_ubicacion_activo(serialact,id_ubicacionnueva)
           
        elif  request.form.get('actualizar_estado') == 'actualizar_estado':
           Activo.acutalizar_estado_activo(serialact,id_estadonuevo)
           
        elif request.form.get('actualizar_ubicacion') == 'actualizar_ubicacion':
           Activo.acutalizar_ubicacion_activo(serialact,id_ubicacionnueva)
    return redirect(url_for('crear_dispositivo'))

@app.route("/PROCESAMIENTO_LOTES")
def PROCESAMIENTO_LOTES():
    data2 =Modelos.listar_modelo()
    data3 = Generalidad.listar_Estado()
    data4 = Location.listar_location()
    data5 = Acta_ingreso.listar_actas()
    return render_template('PROCESAMIENTO_LOTES.html', 
                           modelos = data2, estados = data3,ubicaciones= data4, actingresos = data5)
   
@app.route("/create_activo_masivo", methods=['POST'])
def create_activo_masivo():
    if request.method == 'POST':
        Serial = request.form['Serial']
        estado = request.form['estado']
        act_ingreso = request.form['act_ingreso']
        Modelo = request.form['Modelo']
        ubicacion = request.form['ubicacion']
        print ( Serial)
        contador = 0
        serial = Serial.split("\n")
        print ("EL SERIAL 4 ES "+str(serial[3]))
        for ser in serial:
            ser=ser.strip()
            ser=re.sub(r"\s+$", "", ser)
            ser= re.sub(r"\r+", "", ser)
            
            Activo.crear_Activo(ser,estado,act_ingreso,Modelo,ubicacion)
        return redirect(url_for('PROCESAMIENTO_LOTES'))


@app.route("/update_device_lotes", methods=['POST'])
def update_device_lotes():
    
    if request.method == 'POST':
        serialact = request.form['Seriales']
        id_estadonuevo= request.form['NUEVOESTADO']
        id_ubicacionnueva= request.form['NUEVAUBICACION']
        serial = serialact.split("\n")
        
        if request.form.get('actualizar_estado_ubicacion') == 'actualizar_estado_ubicacion':
            for ser in serial:
                ser=ser.strip()
                ser=re.sub(r"\s+$", "", ser)
                ser= re.sub(r"\r+", "", ser)
                Activo.acutalizar_estado_activo(ser,id_estadonuevo)
                Activo.acutalizar_ubicacion_activo(ser,id_ubicacionnueva)
           
        elif  request.form.get('actualizar_estado') == 'actualizar_estado':
                for ser in serial:
                    ser=ser.strip()
                    ser=re.sub(r"\s+$", "", ser)
                    ser= re.sub(r"\r+", "", ser)
                    Activo.acutalizar_estado_activo(ser,id_estadonuevo)
           
        elif request.form.get('actualizar_ubicacion') == 'actualizar_ubicacion':
           for ser in serial:
                ser=ser.strip()
                ser=re.sub(r"\s+$", "", ser)
                ser= re.sub(r"\r+", "", ser)
                Activo.acutalizar_ubicacion_activo(ser,id_ubicacionnueva)
        return redirect(url_for('PROCESAMIENTO_LOTES'))



@app.route("/Exportar_inventario_tienda" , methods=['POST'])    
def exportar_inventario_tienda():
    sap_buscar="6030"
    if request.method == 'POST':
        sap_buscar = request.form['ubicacion_excel']
   
    result = Activo.filtrar_tienda(sap_buscar)
    #output in byte
    output = io.BytesIO()
    #create WorkBook object
    workbook = xlwt.Workbook()
    #add a sheet
    style2 = xlwt.XFStyle()#inicialización
    style = xlwt.XFStyle()#inicialización
    # Configuración básica de fuente
    font = xlwt.Font()
    font2 = xlwt.Font()
    # Establecer color de fondo
    pattern = xlwt.Pattern()
    # Establecer alineación de celda
    alignment = xlwt.Alignment()
    # Establecer borde
    borders = xlwt.Borders()
    #DEFINIR TIPOGRAFIA Y TAMANO DE LA MISMA
    font.name = u'Arial'
    font.height = 11*20 
    font.bold = True
    
    font2.name = u'Arial'
    font2.height = 11*20 
    font2.bold = False
    borders = xlwt.Borders()
    k=1
    borders.left = k
    borders.right = k
    borders.top = k
    borders.bottom = k
    
    # Establecer alineación de celda
    alignment = xlwt.Alignment()
    # 0x01 (alineado en el extremo izquierdo), 0x02 (alineado en el centro en la dirección horizontal), 0x03 (alineado en el extremo derecho)
    alignment.horz = 0x02
    # 0x00 (alineado en la parte superior), 0x01 (alineado en el centro en la dirección vertical), 0x02 (alineado en la parte inferior)
    alignment.vert = 0x01

    #Puede configurar el ajuste automático de la línea
    #alignment.wrap = 1
        
    
    
    style.font = font
    style.pattern = pattern
    style.alignment = alignment
    style.borders = borders
    style2.font = font2
    style2.pattern = pattern
    style2.alignment = alignment
    style2.borders = borders
    
    
    sh = workbook.add_sheet(sap_buscar)

    ancho =35
    ancho = int(ancho)
    sh.col(0).width = ancho * 26
    sh.col(1).width = ancho * 140
    sh.col(2).width = ancho * 145
    sh.col(3).width = ancho * 80
    sh.col(4).width = ancho * 145
    sh.col(5).width = ancho * 105
    sh.col(6).width = ancho * 115
    sh.col(7).width = ancho * 26
    
    
    
    sh.write_merge(0, 0, 0, 7,'ACTA DE TRASLADO DE ACTIVOS FIJOS ', style)
#/home/despliegues-bogota/KARDEX/KARDEX/Logo-Koba.png 
    Image.open('Logo-Koba.png').convert('RGB').save('Logo-Koba.bmp')  
    #Image.open('/home/despliegues-bogota/KARDEX/KARDEX/Logo-Koba.png').convert('RGB').save('Logo-Koba.bmp')
    sh.insert_bitmap('Logo-Koba.bmp',2,5)
    sh.write_merge(1, 7, 5, 6,)
    
    
    
    
    
    
    fecha = date.today()
    fecha= str(fecha)  
    sh.write(1,1, 'Fecha :',style)
    sh.write(1,2, fecha,style2)
    sh.write(2,1, 'Origen :',style)
    sh.write(2,2, 'BODEGAS SISTEMAS',style2 )
    sh.write(3,1, 'COD ORIGEN :',style)
    sh.write(3,2, '6030',style2 )
    sh.write(4,1, 'DESTINO',style)
    destino=result[0]
    destino=destino[10]
    sh.write(4,2,destino ,style2)
    sh.write(5,1, 'COD DESTINO :',style)
    sh.write(5,2, sap_buscar,style2 )
    sh.write(6,1, 'MOTIVO :',style)
    sh.write(6,2, 'APERTURA',style2 )
    sh.write(7,1, 'DIRECCION :',style)
    sh.write(7,2, '__' ,style2)
    
    sh.write(9,1,'TIPO DEL ACTIVO',style)
    sh.write(9,2,'MARCA',style)
    sh.write(9,3,'MODELO',style)
    sh.write(9,4,'SERIAL',style)
    sh.write(9,5,'ESTADO',style)
    sh.write(9,6,'COMENTARIO',style)
   
    
    
    idx = 9
    
    for row in result:
        
        sh.write(idx+1, 1, (row[8]),style2)
        sh.write(idx+1, 2, (row[7]),style2)
        sh.write(idx+1, 3, (row[6]),style2)
        sh.write(idx+1, 4, (row[0]),style2)
        sh.write(idx+1, 5, (row[4]),style2)
        sh.write(idx+1, 6, (row[2]),style2)
        
        
        idx += 1
    idx +=3
    sh.write_merge(idx, idx, 1, 3,'ENTREGA', style)
    sh.write_merge(idx, idx, 4, 6,'RECIBE', style)
    
    idx +=1
    sh.write_merge(idx, idx, 1, 3,'FECHA : ___ /___ / ______ ', style2)
    sh.write_merge(idx, idx, 4, 6,'FECHA : ___ /___ / ______ ', style2)
    
    idx +=1
    sh.write_merge(idx, idx, 1, 3,'NOMBRE : _____________________', style2)
    sh.write_merge(idx, idx, 4, 6,'NOMBRE : _____________________', style2)
    
    idx +=1
    sh.write_merge(idx, idx, 1, 3,'CARGO : ASISTENTE DE TECNOLOGIA', style2)
    sh.write_merge(idx, idx, 4, 6,'CARGO : JEFE DE ZONA', style2)
    
    idx +=1
    idxm= idx+3
    sh.write_merge(idx, idxm, 1, 3,'', style2)
    sh.write_merge(idx, idxm, 4, 6,'', style2)
    idx=idxm+1
    sh.write_merge(idx, idx, 1, 3,'FIRMA', style)
    sh.write_merge(idx, idx, 4, 6,'FIRMA', style)
    
    
    desti=result[0]
    desti = desti[9]
    etiquetas="LABEL-"+str(desti)
    #\n    
    sh2 = workbook.add_sheet(etiquetas)    
    
    x=int(0)
    y=int(0)
    for row in result:
        #VISOR DE PESO
        #SERIAL: 271481
        # MARCA: ZEBRA
        # MODELO: MX201
        escribir = str(row[8])+"\nSERIAL: "+str(row[0])+"\nMARCA: "+str(row[7])+"\nMODELO: "+str(row[6])+"\n"+str(row[12])
        sh2.write(y,x, str(escribir),style2)
        y=y+1
        if y == 10:
            x = x+1
            y = int(0)
            
        
    
    
    

    workbook.save(output)
    output.seek(0)
    return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=Inventario_"+sap_buscar+".xls"})

    
@app.route("/Export_inventario")
def Export_inventario():
    result = Activo.listar_activo()
    #output in byte
    output = io.BytesIO()
    #create WorkBook object
    workbook = xlwt.Workbook()
    #add a sheet
    sh = workbook.add_sheet('INVENTARIO_6040')
    #FORMATO CABECERA
    style2 = xlwt.XFStyle()#inicialización
    style = xlwt.XFStyle()#inicialización
    # Configuración básica de fuente
    font = xlwt.Font()
    font2 = xlwt.Font()
    # Establecer color de fondo
    pattern = xlwt.Pattern()
    # Establecer alineación de celda
    alignment = xlwt.Alignment()
    # Establecer borde
    borders = xlwt.Borders()
    #DEFINIR TIPOGRAFIA Y TAMANO DE LA MISMA
    font.name = u'Arial'
    font.height = 11*20 
    font.bold = True
    
    font2.name = u'Arial'
    font2.height = 11*20 
    font2.bold = False
    borders = xlwt.Borders()
    k=1
    borders.left = k
    borders.right = k
    borders.top = k
    borders.bottom = k
    
    # Establecer alineación de celda
    alignment = xlwt.Alignment()
    # 0x01 (alineado en el extremo izquierdo), 0x02 (alineado en el centro en la dirección horizontal), 0x03 (alineado en el extremo derecho)
    alignment.horz = 0x02
    # 0x00 (alineado en la parte superior), 0x01 (alineado en el centro en la dirección vertical), 0x02 (alineado en la parte inferior)
    alignment.vert = 0x01

    #Puede configurar el ajuste automático de la línea
    #alignment.wrap = 1
        
    
    
    style.font = font
    style.pattern = pattern
    style.alignment = alignment
    style.borders = borders
    style2.font = font2
    style2.pattern = pattern
    style2.alignment = alignment
    style2.borders = borders
    
    
    
    #negrita = sh.add_format({'bold': True})
    #add headers
    sh.write(0, 0, 'SERIAL',style)
    sh.write(0, 1, 'ULTIMA MODIFICACION',style)
    sh.write(0, 2, 'FECHA INGRESO',style)
    sh.write(0, 3, 'OBSERVACION',style)
    sh.write(0, 4, 'ESTADO',style)
    sh.write(0, 5, 'MODELO',style)
    sh.write(0, 6, 'MARCA',style)
    sh.write(0, 7, 'TIPO DE DISPOSITIVO',style)
    sh.write(0, 8, 'NOMBRE TIENDA',style)
    sh.write(0, 9, 'COD REGIONAL',style)

    borders = xlwt.Borders()
    
    
    
    
    
    
    
    
    
    idx = 0
    
    for row in result:
        sh.write(idx+1, 0, (row[0]),style2)
        sh.write(idx+1, 1, (row[1]),style2)
        sh.write(idx+1, 2, "N/A",style2)
        sh.write(idx+1, 3, (row[2]),style2)
        sh.write(idx+1, 4, (row[4]),style2)
        sh.write(idx+1, 5, (row[6]),style2)
        sh.write(idx+1, 6, (row[7]),style2)
        sh.write(idx+1, 7, (row[8]),style2)
        sh.write(idx+1, 8, (row[10]),style2)
        sh.write(idx+1, 9, (row[11]),style2)
       
        
        idx += 1
    workbook.save(output)
    output.seek(0)
    return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=Reporte_inventario.xls"})
    
@app.route("/Export_pos_vs_tiendas")
def Export_pos_vs_tiendas():
    result = Conf_pos.listar_pos()
    #output in byte
    output = io.BytesIO()
    #create WorkBook object
    workbook = xlwt.Workbook()
    #add a sheet
    sh = workbook.add_sheet('POS_Report')
    #FORMATO CABECERA
    #negrita = sh.add_format({'bold': True})
    #add headers
    sh.write(0, 0, 'idConf pos')
    sh.write(0, 1, 'IP POS')
    sh.write(0, 2, 'TIPO POS')
    sh.write(0, 3, 'Modelo cpu')
    sh.write(0, 4, 'Serial cpu')
    sh.write(0, 5, 'Teclado')
    sh.write(0, 6, 'Impresora')
    sh.write(0, 7, 'Tiendas_Cod_Ncr')
    borders = xlwt.Borders()
    
    idx = 0
    
    for row in result:
        sh.write(idx+1, 0, (row[0]))
        sh.write(idx+1, 1, (row[1]))
        sh.write(idx+1, 2, (row[2]))
        sh.write(idx+1, 3, (row[3]))
        sh.write(idx+1, 4, (row[4]))
        sh.write(idx+1, 5, (row[5]))
        sh.write(idx+1, 6, (row[6]))
        sh.write(idx+1, 7, (row[7]))
        
        idx += 1
    workbook.save(output)
    output.seek(0)
    return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=Reporte_parametrizacion_de_hardware_pos.xls"})


if __name__ == '__main__':
    app.run(port=3200, host="0.0.0.0", debug=True)
    #app.run(port=3030, host="0.0.0.0", debug=True)

