# flask db create models
# flask db upgrade

from peewee import *
from playhouse.flask_utils import FlaskDB


db = FlaskDB()

# CLASE PARA PODER CREAR TABLA ADMINISTRADOR


class Datos_Usuario(db.Model):
    nombre = TextField()
    apellido = TextField()
    genero = TextField()
    documento = TextField(primary_key=True)
    direccion = TextField()
    email = TextField()
    telefono = TextField()
    cel = TextField()
    cargo=TextField()
    clave=TextField()

# INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Usuario, CON LA FUNCION: ingresar_datos_usuario, DESDE: APP /crearAdmin
def ingresar_datos_usuario(nom, ape, gene, doc, direc, email, tel, cel, cargo, clave):            
    entrada, creado = Datos_Usuario.get_or_create(nombre=nom, apellido=ape, genero=gene,
                                                documento=doc, direccion=direc, email=email, telefono=tel, cel=cel, cargo=cargo,clave=clave)

# TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: select_U, RETORNAR LISTA: list(query)
def select_U(doc):
    query = Datos_Usuario.select().where(Datos_Usuario.documento == doc).dicts()    
    return list(query)

# EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: edit_U, DESDE: APP /buscarUsuario
def edit_U(nom, ape, gene, doc, direc, email, tel, cel,cargo,clave):
    update = Datos_Usuario.update(nombre=nom, apellido=ape, genero=gene,
                                documento=doc, direccion=direc, email=email, telefono=tel, cel=cel, cargo=cargo,clave=clave).where(Datos_Usuario.documento == doc).execute()

# ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: delete_U, DESDE: APP /buscarUsuario
def delete_U(doc_elim):
    go_delete = Datos_Usuario.delete().where(Datos_Usuario.documento == doc_elim).execute()


# ******************PROVEEDOR*******************

class Datos_Proveedor(db.Model):
    nombre=TextField()
    nit=TextField(primary_key=True)
    direccion=TextField()
    email=TextField()
    telefono=TextField()
    celular=TextField()

# INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: ingresar_datos_proveedor, DESDE: APP /crearProv
def ingresar_datos_proveedor(nombre, nit, direccion, email, telefono, celular):
    entrada, creado = Datos_Proveedor.get_or_create(nombre=nombre, nit=nit, direccion=direccion,
                                email=email, telefono=telefono, celular=celular)

# TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: select_Prov, RETORNAR LISTA: list(query)
def select_Prov(doc):
    query = Datos_Proveedor.select().where(Datos_Proveedor.nit == doc).dicts()
    return list(query)

# EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: edit_Prov, DESDE: APP /burcarProv
def edit_Prov(nombre, nit, direccion, email, telefono, celular):
    update = Datos_Proveedor.update(nombre=nombre, nit=nit, direccion=direccion,
                                email=email, telefono=telefono, celular=celular).where(Datos_Proveedor.nit == nit).execute()

# ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: delete_Prov, DESDE: APP /burcarProv
def delete_Prov(doc_elim):
    go_delete = Datos_Proveedor.delete().where(Datos_Proveedor.nit == doc_elim).execute()


# ********************PRODUCTO******************

class Datos_Producto(db.Model):
    marca=TextField()
    nombre=TextField()
    codigo=TextField(primary_key=True)
    color=TextField()
    procesador=TextField()
    


# INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: ingresar_datos_producto, DESDE: APP /crearProducto
def ingresar_datos_producto(nombre, marca, codigo, color, procesador):
    entrada, creado = Datos_Producto.get_or_create(nombre=nombre, marca=marca, codigo=codigo,
                                color=color, procesador=procesador)


# TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: select_U, RETORNAR LISTA: list(query)
def select_P(doc):
    print('entrar ',doc)
    query = Datos_Producto.select().where(Datos_Producto.codigo == doc).dicts()
    print(list(query))
    return list(query)

# EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: edit_P, DESDE: APP /crearProducto
def edit_P(nombre, marca, codigo, color, procesador):
    update = Datos_Producto.update(nombre=nombre, marca=marca, codigo=codigo,
                                color=color, procesador=procesador).where(Datos_Producto.codigo == codigo).execute()

# ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: delete_P, DESDE: APP /buscarUsuario
def delete_P(doc_elim):
    go_delete = Datos_Producto.delete().where(Datos_Producto.codigo == doc_elim).execute()







# # CLASE PARA CREAR TABLA DE DATOS CLIENTE FINAL


# class Datos_ClienteF(db.Model):
#     nombre_CF = TextField()
#     apellido_CF = TextField()
#     genero_CF = TextField()
#     documento_CF = TextField(primary_key=True)
#     direccion_CF = TextField()
#     email_CF = TextField()
#     telefono_CF = TextField()
#     cel_CF = TextField()

# # ******************ADMINISTRADOR******************

# # INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: datos_admin, DESDE: APP /crearAdmin
# def ingresar_datos_admin(nom, ape, gene, doc, direc, email, tel, cel):
#     entrada, creado = Datos_Admin.get_or_create(nombre_A=nom, apellido_A=ape, genero_A=gene,
#                                                 documento_A=doc, direccion_A=direc, email_A=email, telefono_A=tel, cel_A=cel)


# # TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: delete, RETORNAR LISTA: list(query)
# def select_A(doc):
#     print('entro ', doc)
#     query = Datos_Admin.select().where(Datos_Admin.documento_A == doc).dicts()
#     return list(query)

# # EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: edit, DESDE: APP /buscarAdmin
# def edit_A(nom, ape, gene, doc, direc, email, tel, cel):
#     update = Datos_Admin.update(nombre_A=nom, apellido_A=ape, genero_A=gene,
#                                 documento_A=doc, direccion_A=direc, email_A=email, telefono_A=tel, cel_A=cel).where(Datos_Admin.documento_CF == doc).execute()

# # ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: delete, DESDE: APP /buscarAdmin
# def delete_A(doc_elim):
#     go_delete = Datos_Admin.delete().where(
#         Datos_Admin.documento_A == doc_elim).execute()


# # *****************CLIENTE FINAL********************************


# # INGRESANDO DATOS A LA TABLA DE DATOS: Datos_ClienteF, CON LA FUNCION: datos_admin, DESDE: APP /crearAdmin
# def ingresar_datos_CF(nom, ape, gene, doc, direc, email, tel, cel):
#     entrada, creado = Datos_ClienteF.get_or_create(nombre_CF=nom, apellido_CF=ape, genero_CF=gene,
#                                                 documento_CF=doc, direccion_CF=direc, email_CF=email, telefono_CF=tel, cel_CF=cel)
#     print('datos cliente final')

# # TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_ClienteF, CON LA FUNCION: delete, RETORNAR LISTA: list(query)
# def select_CF(doc):    
#     query = Datos_ClienteF.select().where(Datos_ClienteF.documento_CF == doc).dicts()
#     return list(query)

# # EDITAR UN DATO DE LA TABLA DE DATOS: Datos_ClienteF, CON LA FUNCION: edit, DESDE: APP /buscarAdmin
# def edit_CF(nom, ape, gene, doc, direc, email, tel, cel):
#     update = Datos_ClienteF.update(nombre_CF=nom, apellido_CF=ape, genero_CF=gene,
#                                                 documento_CF=doc, direccion_CF=direc, email_CF=email, telefono_CF=tel, cel_CF=cel).where(Datos_ClienteF.documento_CF == doc).execute()

# # ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_ClienteF, CON LA FUNCION: delete, DESDE: APP /buscarAdmin
# def delete_CF(doc_elim):
#     go_delete = Datos_ClienteF.delete().where(
#         Datos_ClienteF.documento_CF == doc_elim).execute()