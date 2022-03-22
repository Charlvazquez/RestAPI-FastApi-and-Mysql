from tokenize import String
from turtle import color
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine
usuarios = Table("usuarios", meta,
                 Column("id", Integer, primary_key=True),
                 Column("nombre", String(255)), 
                 Column("correo", String(255)),
                 Column("contrasena", String(255)))
#conectar tabla a la bdd
meta.create_all(engine)