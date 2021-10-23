"""
create table datos_clientef
date created: 2021-10-23 20:08:16.696041
"""


def upgrade(migrator):
    with migrator.create_table('datos_clientef') as table:
        table.text('documento_CF')
        table.text('nombre_CF')
        table.text('apellido_CF')
        table.text('genero_CF')
        table.text('direccion_CF')
        table.text('email_CF')
        table.text('telefono_CF')
        table.text('cel_CF')


def downgrade(migrator):
    migrator.drop_table('datos_clientef')
