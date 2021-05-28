#ESTE ES EL CONTROLADOR
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

import Regionales
app = Flask(__name__)


#Conexion Mysql
app.config['MYSQL_HOST'] = '10.26.1.161'
app.config['MYSQL_USER'] = 'bart'
app.config['MYSQL_PASSWORD'] = 'Linux-1234'
app.config['MYSQL_DB'] = 'Kardex_monitor'
mysql = MySQL(app)

#Configurar sesion
app.secret_key = "mysecretkey"

#RUTA PRINCIPAL, INDEX O PAGINA DE INICIO
@app.route('/')
def index():
    return render_template('index.html')

#CARGUE DE LA PAGINA DE LOGIN DE ADMINISTRACION 


#VISTA RETORNANDO BUSQUEDA



if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0", debug=True)
    #app.run(port=3030, host="0.0.0.0", debug=True)

