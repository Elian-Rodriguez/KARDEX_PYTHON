#ESTE ES EL CONTROLADOR
from re import A
import re
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#CREATE USER 'bart'@'%' IDENTIFIED BY 'Linux-1234';

#Conexion Mysql
app.config['MYSQL_HOST'] = '10.26.1.161'
app.config['MYSQL_USER'] = 'bart'
app.config['MYSQL_PASSWORD'] = 'Linux-1234'
app.config['MYSQL_DB'] = 'Kardex_monitor'
mysql = MySQL(app)

#Configurar sesion
app.secret_key = "mysecretkey"


## Funciones  de listar
def listar_regionales():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.Regional;")
    dat = cur.fetchall()
    return dat
    
def listar_comarcas():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.Tiendas;")
    datas = cur.fetchall()
    return datas

def listar_marca():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.Marca;")
    datas = cur.fetchall()
    return datas


def listar_modelo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from Kardex_monitor.modelo;")
    datas = cur.fetchall()
    return datas

def listar_estado():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.estado;")
    datas = cur.fetchall()
    return datas

def listar_tipo_dispositivo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.Tipo_dispositivo;")
    datas = cur.fetchall()
    return datas

def listar_dispositivo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.Activo;")
    datas = cur.fetchall()
    return datas

def historio_dispositivo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.Historial_act;")
    datas = cur.fetchall()
    return datas

def listar_actas_recibido():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Kardex_monitor.ACT_Ingreso;") 
    datas = cur.fetchall()
    return datas   
















#RUTA PRINCIPAL, INDEX O PAGINA DE INICIO
@app.route('/')
def index():
    return render_template('index.html')

#CARGUE DE LA PAGINA DE LOGIN DE ADMINISTRACION 
@app.route('/Regional')
def Regional():
    data = listar_regionales()
    return render_template('Regional.html',regionales =  data)

@app.route('/create_regional', methods=['POST'])
def create_regional():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        IdRegional=request.form['Id_Regional']
        CODIGOSAP=request.form['CODIGO_SAP']
        NombreRegional=request.form['Nombre_Regional']
        cur.execute('INSERT INTO `Kardex_monitor`.`Regional` (`Cod_Regional`, `Codigo_Sap`, `Nombre_Regional`) VALUES(%s, %s, %s); ',
                        (IdRegional, CODIGOSAP, NombreRegional))
        mysql.connection.commit()
        flash('COMARCA INGRESADA CORRECTAMENTE')
        return Regional()
    



@app.route('/Ubicacion')
def Ubicacion():
    data=listar_comarcas()
    data2= listar_regionales()
    
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
        return Regional()
    #INSERT INTO `Kardex_monitor`.`Tiendas` (`Cod_Ncr`, `Nombre_Tienda`, `Codigo_sap`, `Ip_Server`, `Ip_Pc`, `Ip_Camaras`, `Abierta`, `Estado`, `Regional_Cod_Regional`) VALUES ('2', 'LABORATORIO', '6A06', '10.26.1.161', '10.26.1.161', '10.26.1.161', '1', 'OFFLINE', '6030');

    return Ubicacion()
#VISTA RETORNANDO BUSQUEDA


app.route("/Marca")
def Marca():
    return render_template('Marca.html')
    



if __name__ == '__main__':
    app.run(port=3200, host="0.0.0.0", debug=True)
    #app.run(port=3030, host="0.0.0.0", debug=True)

