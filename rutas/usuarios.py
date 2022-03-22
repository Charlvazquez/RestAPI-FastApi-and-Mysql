from unittest import result
from fastapi import APIRouter, Response
from config.db import conn
from models.usuario import usuarios
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()  # modulo para encriptar con caracteres aleatorios
f = Fernet(key)

# se declara aqui el nombre de la ruta para nuestros endpoints
usuario = APIRouter()

# similar a la ruta de prueba aqui cambiaremos el app por el nombre de la ruta que usemos
@usuario.get('/usuarios')
def get_usuarios():
    return conn.execute(usuarios.select()).fetchall()


@usuario.get('/usuario/{id}')
def get_usuario(id: str):
    return conn.execute(usuarios.select().where(usuarios.c.id == id)).first()


@usuario.post('/usuarios')
def crearUsuario(usuario: User):
    new_usuario = {"nombre": usuario.nombre, "correo": usuario.correo}
    new_usuario["contrasena"] = f.encrypt(usuario.contrasena.encode("utf-8"))
    result = conn.execute(usuarios.insert().values(new_usuario))
    return conn.execute(usuarios.select().where(usuarios.c.id == result.lastrowid)).first()


@usuario.delete('/usuario/{id}')
def borrarUsuario(id: str):
    result = conn.execute(usuarios.delete().where(usuarios.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@usuario.put('/usuario/{id}')
def actualizar(id: str, usuario: User):
    conn.execute(usuarios.update().values(nombre=usuario.nombre,
                                          correo=usuario.correo,
                                        contrasena=f.encrypt(usuario.contrasena.encode("utf-8"))).where(usuarios.c.id == id))
    return  conn.execute(usuarios.select().where(usuarios.c.id == id)).first()                                      
