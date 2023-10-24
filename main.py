from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
#Ayuda a crear un modelo, para ser escalable
from pydantic import BaseModel
from typing import Optional

#instancia de fastapi
#uvicorn main:app --reload --port 5000 -host 0.0.0.0 
#con el comando de arriba estara disponible la app en los dispositivos de la red
app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

#clase movie/esquema
class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar 2",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2010",
		"rating": 8.8,
		"category": "Acción"
	}
]

#endpoint
#los tags nos permite agrupar las rutas de la aplicacion
@app.get("/", tags=['home'])
def read_root():
    return HTMLResponse('<h1>Hello world</h1>')

#mostrar las peliculas
@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

#acceder por id
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []
#mostrar peliculas por categoria
@app.get('/movies/', tags=['movies'])
#se añaden parametros ->()
def get_movies_by_category(category: str):
     return [ item for item in movies if item['category'] == category ]

#Añadir una nueva pelicula
@app.post('/movies', tags=['movies'])
def create_movie(movie:Movie):
    movies.append(movie)
    return movies

#Actualizar una pelicula
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie:Movie):
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return movies
#Eliminar una pelicula
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies