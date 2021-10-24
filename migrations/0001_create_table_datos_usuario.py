"""
create table datos_usuario
date created: 2021-10-24 01:44:59.325051
"""


def upgrade(migrator):
    with migrator.create_table('datos_usuario') as table:
        table.text('documento')
        table.text('nombre')
        table.text('apellido')
        table.text('genero')
        table.text('direccion')
        table.text('email')
        table.text('telefono')
        table.text('cel')
        table.text('cargo')
        table.text('clave')


def downgrade(migrator):
    migrator.drop_table('datos_usuario')
