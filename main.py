from fastapi import FastAPI
from fastapi.responses import HTMLResponse
#instancia de fastapi
#uvicorn main:app --reload --port 5000 -host 0.0.0.0 
#con el comando de arriba estara disponible la app en los dispositivos de la red
app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

#endpoint
#los tags nos permite agrupar las rutas de la aplicacion
@app.get("/", tags=['home'])
def read_root():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies