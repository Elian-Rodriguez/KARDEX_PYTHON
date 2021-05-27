from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
#from werkzeug.contrib.sessions import FilesystemSessionStore

app = Flask(__name__)


#Conexion Mysql
app.config['MYSQL_HOST'] = '10.26.1.161'
app.config['MYSQL_USER'] = 'lisa'
app.config['MYSQL_PASSWORD'] = 'Linux-1234'
app.config['MYSQL_DB'] = 'INVENTARIO_BOGOTA'
mysql = MySQL(app)

#Configurar sesion
app.secret_key = "mysecretkey"

#RUTA PRINCIPAL, INDEX O PAGINA DE INICIO
@app.route('/')
def index():
        return render_template('index.html')

#CARGUE DE LA PAGINA REGIONAL 
@app.route('/Regional')
def Regional():
    data=Regional.Listar_Regional()
    return render_template('Regional.html', regionales = data)

#Crear Regional
@app.route('/create_regional' , methods=['POST'])
def create_regional():
    if request.method == 'POST':
        Id_Regional = request.form['Id_Regional']
        CODIGO_SAP = request.form['CODIGO_SAP']
        Nombre_Regional = request.form['Nombre_Regional']
        Regional.create_regional (Id_Regional, CODIGO_SAP,  Nombre_Regional)
        menssanges = 'Store Added Satisfactorily'
        flash(menssanges)
    return Regional()





#ruta ubucacion
@app.route('/Ubicacion')
def Ubicacion():
    cur = mysql.connection.cursor()
    sentens = ('SELECT * FROM INVENTARIO_BOGOTA.Ubicacion;')
    cur.execute(sentens)
    data = cur.fetchall()
    print(data) 
    return render_template('Ubicacion.html', regionales = data)




#VISTA RETORNANDO BUSQUEDA
@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        buscar = request.form['Buscador']
        print(buscar)
        sentens = (
            'SELECT * FROM TIENDAS.Tienda where Tienda.NOMBRE like"%'+buscar+'%";')
        cur.execute(sentens)
        data = cur.fetchall()
    return render_template('Search.html', shops=data)

#INDEX PARA ADMINISTRADOR  O PAGIANA DE ADMINISTRACION
@app.route('/index_admin',  methods=['POST'])
def index_admin():
    if request.method == 'POST':
        usuario = request.form['user']
        password = request.form['pass']
        print("usuario : " + usuario)
        print("clave : " + password)
        if (usuario == "Homero" and password == "Linux-2020"):
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM Tienda ;")
            #cur.execute("SELECT * FROM Tienda ;")
            data = cur.fetchall()
            #print(data)
            cur.execute(
                """SELECT * FROM TIENDAS.Tienda where Tienda.Estado ="OFLINE";""")
            #SELECT Cod_ncr,CODIGO_SAP,IP_SERVER FROM TIENDAS.Tienda where  estado !="ONLINE" AND Abierta !=0;
            data_2 = cur.fetchall()
            menssanges = 'Ingreso Autorizado'
            flash(menssanges)
            return render_template('index_admin.html', shops=data, offlines=data_2)
        else:
            menssanges = 'Ingreso Incorrecto, Intente Nuevamente'
            flash(menssanges)
            return redirect(url_for('login'))

#MENU DE CREACION DE TIENDA NUEVA
@app.route('/add_shop', methods=['POST'])
def add_shop():
    if request.method == 'POST':
        CODIGO_NCR = request.form['CODIGO_NCR']
        NOMBRE_TIENDA = request.form['NOMBRE_TIENDA']
        CODIGO_SAP = request.form['CODIGO_SAP']
        IP_SERVER = request.form['IP_SERVER']
        IP_PC = request.form['IP_PC']
        IP_CAMARAS = request.form['IP_CAMARAS']
        ESTADO = request.form['ESTADO']
        ABIERTA = request.form['ABIERTA']
        #print (NOMBRE_TIENDA)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO TIENDAS.Tienda (Cod_ncr, NOMBRE, CODIGO_SAP, IP_SERVER, IP_PC, IP_CAMARAS, Abierta, Estado) VALUES(%s, %s, %s, %s, %s, %s, %s, %s ); ',
                    (CODIGO_NCR, NOMBRE_TIENDA, CODIGO_SAP, IP_SERVER, IP_PC, IP_CAMARAS, ABIERTA, ESTADO))
        mysql.connection.commit()
        menssanges = 'Store Added Satisfactorily'
        flash(menssanges)
    return redirect(url_for('index_admin'))

#RETORNO DE BUSQUEDA DE TIENDA Y MENU DE EDICION
@app.route('/update_shop/<string:CODIGO_NCR>', methods=['POST'])
def update_shop(CODIGO_NCR):
    if request.method == 'POST':
        #CODIGO_NCR = request.form['CODIGO_NCR']
        IP_SERVER = request.form['IP_SERVER']
        IP_PC = request.form['IP_PC']
        IP_CAMARAS = request.form['IP_CAMARAS']
        ESTADO = request.form['ESTADO']
        ABIERTA = request.form['ABIERTA']
        #print (NOMBRE_TIENDA)
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE TIENDAS.Tienda
            SET IP_SERVER = %s, 
            IP_PC =  %s, 
            IP_CAMARAS=  %s, 
            Abierta =  %s, 
            Estado =  %s 
        WHERE (Cod_ncr = %s);       
        """, (IP_SERVER, IP_PC, IP_CAMARAS, ABIERTA, ESTADO, CODIGO_NCR))
        mysql.connection.commit()
        menssanges = 'Store Update Satisfactorily'
        flash(menssanges)
        return redirect(url_for('index_admin'))

#ACTUALIZACION DE TIENSA SOLO PERMITE IP Y ESTADO
@app.route('/edit_shop/<string:CODIGO_NCR>')
def get_shop(CODIGO_NCR):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Tienda where Cod_ncr ={0}'.format(CODIGO_NCR))
    data = cur.fetchall()
    print(data[0])
    return render_template('edit-shop.html', shop=data[0])

#ELIMINAR TIENDA 
@app.route('/delete_shop/<string:CODIGO_NCR>')
def delete_shop(CODIGO_NCR):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM TIENDAS.Tienda WHERE (`Cod_ncr` = {0});'.format(CODIGO_NCR))
    mysql.connection.commit()
    menssanges = 'Store Removed Satisfactorily'
    flash(menssanges)
    return redirect(url_for('index_admin'))




if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0", debug=True)
    #app.run(port=3030, host="0.0.0.0", debug=True)
#,host="0.0.0.0"
