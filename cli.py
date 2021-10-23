from app import *
from playhouse.shortcuts import model_to_dict

@app.cli.command('crear_datos')    
def ingresar_datos_admin(nom, ape, gene, doc, direc, email, tel, cel):
    db.init_app(app)
    entrada, creado= Datos_Admin.get_or_create(nombre_A=nom, apellido_A=ape, genero_A=gene,
                                        documento_A=doc, direccion_A=direc, email_A=email, telefono_A=tel, cel_A=cel)
    print(entrada)