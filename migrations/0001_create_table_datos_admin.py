"""
create table datos_admin
date created: 2021-10-22 22:25:23.035909
"""


def upgrade(migrator):
    with migrator.create_table('datos_admin') as table:
        table.text('documento_A')
        table.text('nombre_A')
        table.text('apellido_A')
        table.text('genero_A')
        table.text('direccion_A')
        table.text('email_A')
        table.text('telefono_A')
        table.text('cel_A')


def downgrade(migrator):
    migrator.drop_table('datos_admin')
