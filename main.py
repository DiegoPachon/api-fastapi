from fastapi import FastAPI
#instancia de fastapi
#uvicorn main:app --reload --port 5000 -host 0.0.0.0 
#con el comando de arriba estara disponible la app en los dispositivos de la red
app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"
#endpoint
#los tags nos permite agrupar las rutas de la aplicacion
@app.get("/", tags=['home'])
def read_root():
    return {"Hello": "World"}