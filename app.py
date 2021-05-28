from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#from werkzeug.contrib.sessions import FilesystemSessionStore

app = Flask(__name__)


#Conexion Mysql
app.config['MYSQL_HOST'] = '10.26.1.161'
app.config['MYSQL_USER'] = 'lisa'
app.config['MYSQL_PASSWORD'] = 'Linux-1234'
app.config['MYSQL_DB'] = 'Kardex_monitor'
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
    data=Regionald.Listar_Regional()
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
    sentens = ('SELECT * FROM Kardex_monitor.Tiendas;')
    cur.execute(sentens)
    data = cur.fetchall()
    print(data) 
    return render_template('Ubicacion.html', regionales = data)









if __name__ == '__main__':
    app.run(port=3000,  debug=True)
    #app.run(port=3030, host="0.0.0.0", debug=True)
#,host="0.0.0.0"
