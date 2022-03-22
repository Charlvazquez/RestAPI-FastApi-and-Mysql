from fastapi import FastAPI #importar FastAPI
from rutas.usuarios import usuario #se importa el archivo donde viene nuestras rutas

#creacion de servidor
#al momento de correr el servidor sera con app:el nombre del archivo que contenga el server

app = FastAPI()
#declaracion de usar las rutas de usuario
app.include_router(usuario)

#ruta de prueba
#@app.get('/')
#def test():
#    return "hola mundo"