from flask import Flask,redirect,url_for,render_template,request

from models import *
from config import dev

# from cli import ingresar_datos_admin

app=Flask(__name__)
app.config.from_object(dev)

db.init_app(app)

@app.route('/',methods=['GET','POST'])
def index():    
    return render_template("layout.html")
# CREAR ADMINISTRADOR
@app.route("/crearAdmin", methods=["GET", "POST"])
def crearAdmin():

    if 'ingresar' in request.values:
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        genero=request.form.get('genero')
        documento=request.form.get('documento')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        cel=request.form.get('cel')    
        
        ingresar_datos_admin(nombre,apellido,genero,documento,direccion,email,telefono,cel)

    return render_template("crearAdmin.html")

# BUSCARA ADMINISTRADOR
@app.route("/buscarAdmin", methods=["GET", "POST"])
def buscarAdmin():
    
    if 'buscar' in request.values:
        doc_bus=request.form.get('doc_buscar')        
        print(doc_bus)
        datos=select_A(doc_bus)        
        return render_template("buscarAdmin.html", datos=datos)
            
    
    if 'editar' in request.values:
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        genero=request.form.get('genero')
        documento=request.form.get('documento')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        cel=request.form.get('cel')
        edit_A(nombre,apellido,genero,documento,direccion,email,telefono,cel)
        datos=select_A(documento)
        return render_template("buscarAdmin.html", datos=datos)    
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('documento')
        delete_A(doc_elim)
        return render_template("buscarAdmin.html")
    else:
        return render_template("buscarAdmin.html")
    
    
    

# CREAR CLIENTE FINAL
@app.route("/crearClienteFinal", methods=["GET", "POST"])
def crearClienteFinal():
    return render_template("crearClienteFinal.html")

# BUSCAR CLIENTE FINAL
@app.route("/buscarClienteFinal", methods=["GET", "POST"])
def buscarClienteFinal():
    return render_template("buscarClienteFinal.html")

if __name__ == '__main__':
    
    app.run()