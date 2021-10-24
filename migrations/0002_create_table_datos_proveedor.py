"""
create table datos_proveedor
date created: 2021-10-24 13:25:14.244211
"""


def upgrade(migrator):
    with migrator.create_table('datos_proveedor') as table:
        table.text('nit')
        table.text('nombre')
        table.text('direccion')
        table.text('email')
        table.text('telefono')
        table.text('celular')


def downgrade(migrator):
    migrator.drop_table('datos_proveedor')
