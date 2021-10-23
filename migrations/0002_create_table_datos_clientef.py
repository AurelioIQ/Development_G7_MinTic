"""
create table datos_clientef
date created: 2021-10-22 22:25:23.056896
"""


def upgrade(migrator):
    with migrator.create_table('datos_clientef') as table:
        table.char('documento_CF', max_length=255)
        table.char('nombre_CF', max_length=255)
        table.char('apellido_CF', max_length=255)
        table.char('genero_CF', max_length=255)
        table.char('direccion_CF', max_length=255)
        table.char('email_CF', max_length=255)
        table.char('telefono_CF', max_length=255)
        table.char('cel_CF', max_length=255)


def downgrade(migrator):
    migrator.drop_table('datos_clientef')
