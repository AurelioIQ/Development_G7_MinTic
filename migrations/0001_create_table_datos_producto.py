"""
create table datos_producto
date created: 2021-10-24 13:25:14.234219
"""


def upgrade(migrator):
    with migrator.create_table('datos_producto') as table:
        table.text('codigo')
        table.text('marca')
        table.text('nombre')
        table.text('color')
        table.text('procesador')


def downgrade(migrator):
    migrator.drop_table('datos_producto')
