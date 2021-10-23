# flask db create models
# flask db upgrade

from peewee import *
from playhouse.flask_utils import FlaskDB


db=FlaskDB()

# CLASE PARA PODER CREAR TABLA ADMINISTRADOR
class Datos_Admin(db.Model):
    nombre_A = TextField()
    apellido_A = TextField()
    genero_A = TextField()
    documento_A = TextField(primary_key=True)
    direccion_A = TextField()
    email_A = TextField()
    telefono_A = TextField()
    cel_A = TextField()

# CLASE PARA CREAR TABLA DE DATOS CLIENTE FINAL
class Datos_ClienteF(db.Model):
    nombre_CF = CharField()
    apellido_CF = CharField()
    genero_CF = CharField()
    documento_CF = CharField(primary_key=True)
    direccion_CF = CharField()
    email_CF = CharField()
    telefono_CF = CharField()
    cel_CF = CharField()


# INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: datos_admin, DESDE: APP /crearAdmin
def ingresar_datos_admin(nom, ape, gene, doc, direc, email, tel, cel):    
    if not doc in Datos_Admin.documento_A:
        entrada, creado= Datos_Admin.get_or_create(nombre_A=nom, apellido_A=ape, genero_A=gene,
                                            documento_A=doc, direccion_A=direc, email_A=email, telefono_A=tel, cel_A=cel)
        print(entrada)

# TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: delete, RETORNAR LISTA: list(query)
def select_A(doc):
    print('entro ',doc)   
    query = Datos_Admin.select().where(Datos_Admin.documento_A==doc).dicts()
    return list(query)

# EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: edit, DESDE: APP /buscarAdmin
def edit_A(nom,ape,gene,doc,direc,email,tel,cel):
    update = Datos_Admin.update(nombre_A=nom, apellido_A=ape, genero_A=gene,
                                documento_A=doc, direccion_A=direc, email_A=email, telefono_A=tel, cel_A=cel).where(Datos_Admin.documento_A == doc).execute()

# ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: delete, DESDE: APP /buscarAdmin
def delete_A(doc_elim):    
    go_delete = Datos_Admin.delete().where(Datos_Admin.documento_A == doc_elim).execute()
