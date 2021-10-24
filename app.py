from flask import Flask,redirect,url_for,render_template,request

from models import *
from config import dev

app=Flask(__name__)
app.config.from_object(dev)

db.init_app(app)

@app.route('/',methods=['GET','POST'])
def index():    
    return render_template("layout.html")

# ****************ADMINISTRADOR*********************

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
        cargo=request.form.get('cargo')
        clave=request.form.get('clave')
        
        ingresar_datos_usuario(nombre,apellido,genero,documento,direccion,email,telefono,cel,cargo,clave)

    return render_template("crearAdmin.html")

   

# ********************CLIENTE FINAL**************************

# CREAR CLIENTE FINAL
@app.route("/crearClienteFinal", methods=["GET", "POST"])
def crearClienteFinal():

    if 'ingresar' in request.values:        
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        genero=request.form.get('genero')
        documento=request.form.get('documento')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        cel=request.form.get('cel')
        cargo=request.form.get('cargo')
        clave=request.form.get('clave')
        
        ingresar_datos_usuario(nombre,apellido,genero,documento,direccion,email,telefono,cel,cargo,clave)
    
    return render_template("crearClienteFinal.html")

# ***************BUSCAR USUARIO GENERAL***************

# BUSCARA USUARIO
@app.route("/buscarUsuario", methods=["GET", "POST"])
def buscarAdmin():
    
    if 'buscar' in request.values:
        doc_bus=request.form.get('doc_buscar')        
        print(doc_bus)
        datos=select_U(doc_bus)
        return render_template("buscarUsuario.html", datos=datos)
            
    
    if 'editar' in request.values:
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        genero=request.form.get('genero')
        documento=request.form.get('documento')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        cel=request.form.get('cel')
        cargo=request.form.get('cargo')
        clave=request.form.get('clave')

        edit_U(nombre,apellido,genero,documento,direccion,email,telefono,cel,cargo,clave)
        datos=select_U(documento)
        return render_template("buscarUsuario.html", datos=datos)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('documento')
        delete_U(doc_elim)
        return render_template("buscarUsuario.html")
    else:
        return render_template("buscarUsuario.html")

# **************CREEAR PROVEEDOR*****************

@app.route("/crearProv",methods=["GET", "POST"])
def crearProv():
    if 'ingresar' in request.values:
        nombre=request.form.get('nombre')
        nit=request.form.get('nit')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        celular=request.form.get('celular')

        ingresar_datos_proveedor(nombre, nit, direccion, email, telefono, celular)

    return render_template('crearProv.html')

# BUSCARA PROVEEDOR
@app.route("/buscarProv", methods=["GET", "POST"])
def buscarProv():
    
    if 'buscar' in request.values:
        nit_bus=request.form.get('nit_bus')
        datos=select_Prov(nit_bus)
        return render_template("buscarProv.html", datos=datos)
            
    
    if 'editar' in request.values:
        nombre=request.form.get('nombre')
        nit=request.form.get('nit')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        celular=request.form.get('cel')

        edit_Prov(nombre, nit, direccion, email, telefono, celular)
        datos=select_Prov(nit)

        return render_template("buscarProv.html", datos=datos)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('nit')
        delete_Prov(doc_elim)
        return render_template("buscarProv.html")
    else:
        return render_template("buscarProv.html")



# **************CREAR PRODUCTO*******************


@app.route("/crearProduc",methods=["GET", "POST"])
def crearProduc():

    if 'ingresar' in request.values:
        marca=request.form.get('marca')
        nombre=request.form.get('nombre')
        codigo=request.form.get('codigo')
        color=request.form.get('color')
        procesador=request.form.get('procesador')

        ingresar_datos_producto(marca,nombre,codigo,color,procesador)

    return render_template('crearProduc.html')

# BUSCARA PRODUCTO
@app.route("/buscarProduc", methods=["GET", "POST"])
def buscarProduc():
    
    if 'buscar' in request.values:
        cod_bus=request.form.get('cod_bus')
        datos=select_P(cod_bus)
        return render_template("buscarProduc.html", datos=datos)
            
    
    if 'editar' in request.values:
        marca=request.form.get('marca')
        nombre=request.form.get('nombre')
        codigo=request.form.get('codigo')
        color=request.form.get('color')
        procesador=request.form.get('procesador')

        edit_P(marca,nombre,codigo,color,procesador)
        datos=select_P(codigo)
        return render_template("buscarProduc.html", datos=datos)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('codigo')
        delete_P(doc_elim)
        return render_template("buscarProduc.html")
    else:
        return render_template("buscarProduc.html")

# # BUSCAR CLIENTE FINAL
# @app.route("/buscarClienteFinal", methods=["GET", "POST"])
# def buscarClienteFinal():
#     if 'buscar' in request.values:
#         doc_bus=request.form.get('doc_buscar')
#         datos=select_U(doc_bus)        
#         return render_template("buscarUsuario.html", datos=datos)
            
    
#     if 'editar' in request.values:
#         nombre=request.form.get('nombre')
#         apellido=request.form.get('apellido')
#         genero=request.form.get('genero')
#         documento=request.form.get('documento')
#         direccion=request.form.get('direccion')
#         email=request.form.get('email')
#         telefono=request.form.get('telefono')
#         cel=request.form.get('cel')
#         cargo=request.form.get('cargo')
#         clave=request.form.get('clave')
        
#         edit_U (nombre,apellido,genero,documento,direccion,email,telefono,cel,cargo,clave)
#         datos=select_U(documento)
#         return render_template("buscarUsuario.html", datos=datos)    
    
#     if 'eliminar' in request.values:
#         doc_elim=request.form.get('documento')
#         delete_U(doc_elim)
#         return render_template("buscarUsuario.html")
#     else:
#         return render_template("buscarUsuario.html")
    

if __name__ == '__main__':
    
    app.run()